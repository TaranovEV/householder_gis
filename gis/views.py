import folium
import geopy.distance
from gis import calculate_geometry
from . import getiso
from django.shortcuts import render
from django.views.generic.base import TemplateView


class MapView(TemplateView):
    """Base map view."""
    template_name = "map.html"


def showzone(request, lat, lon, type_iso, time_iso):
    path_house = r"..\householder_gis\data\houses.csv"
    path_shops = r"..\householder_gis\data\opponents.csv"
    path_bus_station = r"..\householder_gis\data\bus_stops.csv"
    path_metro = r"..\householder_gis\data\metro_stations.csv"
    icon_url = r"..\householder_gis\gis\static\marker-icon-2x-orange.png"
    mode_poly = 'circle'
    if mode_poly == 'isochrone':
        graph_poly = getiso.create_graph(G,
                                         type_iso,
                                         (lat, lon),
                                         time_iso)
        iso_poly = getiso.alpha_shape(graph_poly, alpha=13)

    speed = 25
    if type_iso == 'walk':
        speed = 4.5

    lat, lon, time_iso = float(lat), float(lon), float(time_iso)
    dist = speed * float(time_iso) / 60

    houses = calculate_geometry.load_geodataframe(path_house)
    shops = calculate_geometry.load_geodataframe(path_shops)
    bus_station = calculate_geometry.load_geodataframe(path_bus_station)
    final_metro = calculate_geometry.load_geodataframe(path_metro)
    final_metro = (
        final_metro[['NameOfStation', 'IncomingPassengers', 'geometry']]
    )
    iso_poly = calculate_geometry.get_R((lat, lon), dist)
    iso_poly.set_crs(epsg=4326, inplace=True)

    circle_bus = calculate_geometry.get_R((lat, lon), 0.3)
    circle_bus.set_crs(epsg=4326, inplace=True)

    bus_station = (
        bus_station[bus_station.within(circle_bus[0])]
    )
    bus_stop_count = len(bus_station)

    if bus_stop_count != 0:
        routes_count = (
            len(set(bus_station['RouteNumbers'].apply(lambda x: x.split(';')).sum()))
        )
    else:
        routes_count = 0

    quarters_count = (
        houses[houses.within(iso_poly[0])]['quarters_count'].astype(int).sum()
    )
    shops = (
        shops[shops.within(iso_poly[0])]
    )
    shops['distance'] = (
        shops['geometry'].apply(
            lambda cord:
            round(geopy.distance.geodesic((lon, lat), (cord.x, cord.y)).km * 1000))
    )
    metro_in_zone = final_metro[final_metro.within(iso_poly[0])]

    our_shops = shops[shops['Name'] == 'Электротовары']
    opponents = shops[shops['Name'] != 'Электротовары']

    figure = folium.Figure()
    m = folium.Map(location=[lat,lon],
                   zoom_start=15,
                   tiles='cartodbpositron')
    m.add_to(figure)

    icon = folium.features.CustomIcon(icon_url,
                                      icon_size=(18, 30),)
    folium.Marker(
        location=[lat, lon],
        icon=icon
        ).add_to(m)

    layers_to_add = [
        {
            'geodata': opponents,
            'html': f"""<i class="fa fa-shopping-basket" aria-hidden="true" style='color:#E45A50'></i>"""
        },
        {
            'geodata': our_shops,
            'html': f"""<i class="fa fa-bus" aria-hidden="true" style='color:#779FAF'></i>"""
        },
        {
            'geodata': bus_station,
            'html': f"""<i class="fa fa-bus" aria-hidden="true" style='color:#779FAF'></i>"""
        },
        {
            'geodata': metro_in_zone,
            'html': f"""<img src="/static/Mosmetro_logo_M.svg" width="20" class="fill_m">"""
        }
    ]

    for layer in layers_to_add:
        for row in range(len(layer['geodata'])):
            folium.Marker(
                location=[layer['geodata'].iloc[row]['geometry'].y,
                          layer['geodata'].iloc[row]['geometry'].x],
                icon=folium.DivIcon(
                html=layer['html'])).add_to(m)

    folium.GeoJson(iso_poly,
                   style_function=lambda feature: {'color':"#e67744",
                                                   'fillColor':'#c78d73'}).add_to(m)
    opponents_for_render = (
        opponents[['Name', 'Address', 'distance']].to_dict('records')
    )
    our_shops_for_render = (
        our_shops[['Name', 'Address', 'Площадь', 'distance']].to_dict('records')
    )
    metro_count = metro_in_zone.to_dict('records')
    figure.render()

    context = {
        'map': figure,
        'type_iso': 'автомобиль' if type_iso == 'drive_service' else 'пешком',
        'time_iso': int(time_iso),
        'quarters_count': quarters_count,
        'bus_stop_count': bus_stop_count,
        'metro_count': metro_count,
        'routes_count': routes_count,
        'opponents_for_render': opponents_for_render,
        'our_shops_for_render': our_shops_for_render
    }
    return render(request, 'showroute.html', context)

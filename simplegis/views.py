import folium
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import TemplateView

from simplegis import calculate_geometry

from . import getiso
from .models import BusStop, House, Metro, Shop


class MapView(TemplateView):
    """Base map view."""
    template_name = "map.html"


@login_required
def showzone(request, lat, lon, type_iso, time_iso):
    icon_url = r"../householder_gis/simplegis/static/marker-icon-2x-orange.png"
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
    
    quarters_count = House.objects.get_quaters_in_R(lon, lat, dist)['quarters_count']
    shops = Shop.objects.get_shops_in_R(lon, lat, dist)
    our_shops_for_render = shops.filter(name='Электротовары')
    opponents_for_render = shops.filter(~Q(name='Электротовары'))
    bus_station, bus_stop_count, routes_count = BusStop.objects.get_stops_in_R(lon, lat, dist=0.3)
    metro_count = Metro.objects.get_stations_in_R(lon, lat, dist)
    
    iso_poly = calculate_geometry.get_R((lat, lon), dist)
    iso_poly.set_crs(epsg=4326, inplace=True)
    
    
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
            'geodata': opponents_for_render,
            'html': f"""<i class="fa fa-shopping-basket" aria-hidden="true" style='color:#E45A50'></i>"""
        },
        {
            'geodata': our_shops_for_render,
            'html': f"""<i class="fa fa-shopping-basket" aria-hidden="true" style='color:#139d82'></i>"""
        },
        {
            'geodata': bus_station,
            'html': f"""<i class="fa fa-bus" aria-hidden="true" style='color:#779FAF'></i>"""
        },
        {
            'geodata': metro_count,
            'html': f"""<img src="/static/Mosmetro_logo_M.svg" width="20" class="fill_m">"""
        }
    ]

    for layer in layers_to_add:
        for row in layer['geodata']:
            folium.Marker(
                location=[row.geometry.y,
                          row.geometry.x],
                icon=folium.DivIcon(
                html=layer['html'])).add_to(m)

    folium.GeoJson(iso_poly,
                   style_function=lambda feature: {'color':"#e67744",
                                                   'fillColor':'#c78d73'}).add_to(m)
    
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
    return render(request, 'showinfo.html', context)

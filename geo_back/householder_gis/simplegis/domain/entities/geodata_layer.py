from dataclasses import dataclass
from typing import List

from geo_back.householder_gis.simplegis.domain.entities.bus_stops import BusStop
from geo_back.householder_gis.simplegis.domain.entities.isochron import Isochron
from geo_back.householder_gis.simplegis.domain.entities.metro_stations import (
    MetroStation,
)
from geo_back.householder_gis.simplegis.domain.entities.shops import Shop
from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Longitude,
    Latitude,
)


@dataclass(slots=True, kw_only=True)
class GeoDataLayer:
    type_iso: str
    time_iso: int
    quarters_count: int
    bus_station: List[BusStop]
    bus_stop_count: None
    metro_count: List[MetroStation]
    routes_count: int
    opponents_for_render: List[Shop]
    our_shops_for_render: List[Shop]
    pin_coords: List[Longitude, Latitude]
    geometry: Isochron

    # geojson = {
    #     "type": "FeatureCollection",
    #     "features": {
    #         "type": "Feature",
    #         "properties": {
    #             "type_iso": (
    #                 "автомобиль" if type_iso == "drive_service" else "пешком"
    #             ),
    #             "time_iso": time_iso,
    #             "quarters_count": quarters_count,
    #             "bus_station": BusStopSerializer(bus_stops, many=True).data,
    #             "bus_stop_count": bus_stops_count,
    #             "metro_count": MetroStationSerializer(metro_count, many=True).data,
    #             "routes_count": bus_routes_count,
    #             "opponents_for_render": AddDistanceSerializer(
    #                 opponents, many=True
    #             ).data,
    #             "our_shops_for_render": AddDistanceSerializer(
    #                 our_shops, many=True
    #             ).data,
    #             "pin_coords": [longitude, latitude],
    #         },
    #         "geometry": isochron,
    #     },
    # }

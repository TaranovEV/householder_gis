from dataclasses import dataclass
from typing import List

from geo_back.householder_gis.simplegis.domain.entities.bus_stops import BusStop
from geo_back.householder_gis.simplegis.domain.entities.isochrone import Isochrone
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
    bus_routes_count: int
    bus_stop_count: None
    metro_stations: List[MetroStation]
    routes_count: int
    opponents: List[Shop]
    our_shops: List[Shop]
    pin_coords: List[Longitude, Latitude]
    geometry: Isochrone

    def to_geojson(self):
        return {
            "type": "FeatureCollection",
            "features": {
                "type": "Feature",
                "properties": {
                    "type_iso": (
                        "автомобиль" if self.type_iso == "drive_service" else "пешком"
                    ),
                    "time_iso": self.time_iso,
                    "quarters_count": self.quarters_count,
                    "bus_station": self.bus_station,
                    "bus_stop_count": self.bus_stops_count,
                    "metro_count": self.metro_stations,
                    "routes_count": self.bus_routes_count,
                    "opponents_for_render": self.opponents,
                    "our_shops_for_render": self.our_shops,
                    "pin_coords": self.pin_coords,
                },
                "geometry": self.geometry,
            },
        }

from dataclasses import dataclass
from django.contrib.gis.geos import Point

from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)


@dataclass(slots=True, kw_only=True)
class BusStop:
    name: str
    route_numbers: str
    geometry: Point(Longitude, Latitude)

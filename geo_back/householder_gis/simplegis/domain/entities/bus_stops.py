from dataclasses import dataclass
from django.contrib.gis.geos import Point


@dataclass(slots=True, kw_only=True)
class BusStop:
    name: str
    route_numbers: str
    geometry: Point

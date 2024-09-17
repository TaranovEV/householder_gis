from dataclasses import dataclass
from django.contrib.gis.geos import Point


@dataclass(slots=True, kw_only=True)
class MetroStation:
    name: str
    line: str
    incoming_passengers: int
    geometry: Point

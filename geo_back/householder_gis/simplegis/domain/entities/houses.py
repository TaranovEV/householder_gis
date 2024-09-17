from dataclasses import dataclass
from django.contrib.gis.geos import Point


@dataclass(slots=True, kw_only=True)
class House:
    address: str
    quarters_count: int
    geometry: Point

from dataclasses import dataclass
from django.contrib.gis.geos import Point


@dataclass(slots=True, kw_only=True)
class Shop:
    name: str
    address: str
    square: float
    sales: float
    geometry: Point

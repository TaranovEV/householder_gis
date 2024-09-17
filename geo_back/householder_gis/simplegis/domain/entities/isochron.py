from dataclasses import dataclass

from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)


@dataclass(slots=True, kw_only=True)
class Isochron:
    longitude: Longitude
    latitude: Latitude
    radius: float

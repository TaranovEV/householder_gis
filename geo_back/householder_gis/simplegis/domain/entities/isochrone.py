from dataclasses import dataclass, field

from django.contrib.gis.geos import Point

from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)


@dataclass(slots=True, kw_only=True)
class Isochrone:
    longitude: Longitude
    latitude: Latitude
    center: Point = field(init=False)
    inner_radius: float = 0.3
    radius: float = field(init=False)
    speed = 25
    type_iso: str
    time_iso: int
    transform_constanta = 60

    def __post_init__(self):
        self.center = Point(self.longitude, self.latitude)
        if self.type_iso == "walk":
            self.speed = 4.5

        self.radius = self.speed * self.time_iso / self.transform_constanta

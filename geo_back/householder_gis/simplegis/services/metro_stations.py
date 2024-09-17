from dataclasses import dataclass, field

from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)
from geo_back.householder_gis.simplegis.infra.repositories.metro_stations import (
    ORMMetroStations,
)


@dataclass(slots=True, kw_only=True)
class MetroStationsService:
    longitude: Longitude
    latitude: Latitude
    distance: float
    orm_service: ORMMetroStations = field(init=False)

    def __post_init__(self):
        self.orm_service = ORMMetroStations(
            longitude=self.longitude, latitude=self.latitude, distance=self.distance
        )

    def get_stations_inside_circle_zone(self):
        return self.orm_service.filter_stations_inside(
            longitude=self.longitude, latitude=self.latitude, distance=self.distance
        )

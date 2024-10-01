from dataclasses import dataclass, field

from geo_back.householder_gis.simplegis.domain.entities.isochrone import Isochrone
from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)
from geo_back.householder_gis.simplegis.infra.repositories.metro_stations import (
    ORMMetroStations,
)


@dataclass(slots=True, kw_only=True)
class MetroStationsService:
    isochrone: Isochrone
    orm_service: ORMMetroStations = field(init=False)

    def __post_init__(self):
        self.orm_service = ORMMetroStations(isochrone=self.isochrone)

    def get_stations_inside_circle_zone(self):
        return self.orm_service.filter_stations_inside()

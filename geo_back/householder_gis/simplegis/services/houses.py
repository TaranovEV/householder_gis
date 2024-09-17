from dataclasses import dataclass, field
from typing import Union, List

from django.db.models import QuerySet

from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)
from geo_back.householder_gis.simplegis.infra.django_models.models import House
from geo_back.householder_gis.simplegis.infra.repositories.houses import ORMHouses


@dataclass(slots=True, kw_only=True)
class HousesService:
    longitude: Longitude
    latitude: Latitude
    distance: float
    orm_service: ORMHouses = field(init=False)

    def __post_init__(self):
        self.orm_service = ORMHouses(
            longitude=self.longitude, latitude=self.latitude, distance=self.distance
        )

    def get_quaters_inside_circle_zone(self) -> Union[QuerySet, List[House]]:
        return self.orm_service.filter_quaters_inside(
            longitude=self.longitude, latitude=self.latitude, distance=self.distance
        )

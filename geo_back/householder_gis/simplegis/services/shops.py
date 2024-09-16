from dataclasses import dataclass, field
from typing import Union, List

from django.db.models import QuerySet

from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)
from geo_back.householder_gis.simplegis.infra.django_models.models import Shop
from geo_back.householder_gis.simplegis.infra.repositories.shops import ORMShops


@dataclass(slots=True, kw_only=True)
class Shops:
    longitude: Longitude
    latitude: Latitude
    distance: float
    orm_service: ORMShops = field(init=False)

    def __post_init__(self):
        self.orm_service = ORMShops(
            longitude=self.longitude, latitude=self.latitude, distance=self.distance
        )

    def get_our_shops_inside_circle_zone(self) -> Union[QuerySet, List[Shop]]:
        return self.orm_service.filter_our_shops_inside(
            longitude=self.longitude, latitude=self.latitude, distance=self.distance
        )

    def get_competitor_shops_inside_circle_zone(self) -> Union[QuerySet, List[Shop]]:
        return self.orm_service.filter_competitor_shops_inside(
            longitude=self.longitude, latitude=self.latitude, distance=self.distance
        )

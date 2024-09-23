from dataclasses import dataclass, field
from typing import Union, List

from django.db.models import QuerySet

from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)
from geo_back.householder_gis.simplegis.infra.django_models.models import Shop
from geo_back.householder_gis.simplegis.infra.repositories.shops import ORMShops
from geo_back.householder_gis.simplegis.interfaces.serializers.serrializers import (
    AddDistanceSerializer,
)


@dataclass(slots=True, kw_only=True)
class ShopsService:
    longitude: Longitude
    latitude: Latitude
    distance: float
    orm_service: ORMShops = field(init=False)

    def __post_init__(self):
        self.orm_service = ORMShops(
            longitude=self.longitude, latitude=self.latitude, distance=self.distance
        )

    def serialize_data(self, queryset: QuerySet) -> dict:
        return AddDistanceSerializer(queryset, many=True).data

    def get_our_shops_inside_circle_zone(self) -> Union[QuerySet, List[Shop]]:
        queryset = self.orm_service.filter_our_shops_inside(
            longitude=self.longitude, latitude=self.latitude, distance=self.distance
        )
        return self.serialize_data(queryset=queryset)

    def get_competitor_shops_inside_circle_zone(self) -> Union[QuerySet, List[Shop]]:
        queryset = self.orm_service.filter_competitor_shops_inside(
            longitude=self.longitude, latitude=self.latitude, distance=self.distance
        )
        return self.serialize_data(queryset=queryset)

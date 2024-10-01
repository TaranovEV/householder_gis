from dataclasses import dataclass, field
from typing import Union, List

from django.db.models import QuerySet

from geo_back.householder_gis.simplegis.domain.entities.isochrone import Isochrone
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
    isochrone: Isochrone
    orm_service: ORMShops = field(init=False)

    def __post_init__(self):
        self.orm_service = ORMShops(isochrone=self.isochrone)

    def serialize_data(self, queryset: QuerySet) -> dict:
        return AddDistanceSerializer(queryset, many=True).data

    def get_our_shops_inside_circle_zone(self) -> Union[QuerySet, List[Shop]]:
        queryset = self.orm_service.filter_our_shops_inside()
        return self.serialize_data(queryset=queryset)

    def get_competitor_shops_inside_circle_zone(self) -> Union[QuerySet, List[Shop]]:
        queryset = self.orm_service.filter_competitor_shops_inside()
        return self.serialize_data(queryset=queryset)

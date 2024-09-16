from dataclasses import dataclass
from typing import Union, List

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.db.models import Q, QuerySet

from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)
from geo_back.householder_gis.simplegis.infra.django_models.models import (
    Shop as ShopModel,
)


@dataclass(slots=True, kw_only=True)
class ORMShops:
    model: "Shops" = ShopModel
    filters: "ShopsFilters" = None
    longitude: Longitude
    latitude: Latitude
    distance: float

    def filter_our_shops_inside(self) -> Union[QuerySet, List[ShopModel]]:
        point = Point(self.longitude, self.latitude)
        return self.model.filter(
            geometry__distance_lt=(point, Distance(km=self.distance))
            & Q(name="Электротовары")
        )

    def filter_competitor_shops_inside(self) -> Union[QuerySet, List[ShopModel]]:
        point = Point(self.longitude, self.latitude)
        return self.model.filter(
            geometry__distance_lt=(point, Distance(km=self.distance))
            & ~Q(name="Электротовары")
        )

from dataclasses import dataclass
from typing import Union, List

from django.contrib.gis.measure import Distance
from django.db.models import QuerySet, Sum

from geo_back.householder_gis.simplegis.domain.entities.isochrone import Isochrone
from geo_back.householder_gis.simplegis.infra.django_models.models import (
    House as HouseModel,
)


@dataclass(slots=True, kw_only=True)
class ORMHouses:
    isochrone: Isochrone
    model: "Houses" = HouseModel
    filters: "HousesFilters" = None

    def filter_points_inside(self):
        point = self.isochrone.center
        return self.model.filter(
            geometry__distance_lt=(point, Distance(km=self.isochrone.radius))
        )

    def filter_quaters_inside(self) -> Union[QuerySet, List[HouseModel]]:
        return self.filter_points_inside().aggregate(
            quarters_count=Sum("quarters_count")
        )["quarters_count"]

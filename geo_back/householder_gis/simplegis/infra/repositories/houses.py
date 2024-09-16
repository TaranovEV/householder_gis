from dataclasses import dataclass
from typing import Union, List

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.db.models import QuerySet, Sum

from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)
from geo_back.householder_gis.simplegis.infra.django_models.models import (
    House as HouseModel,
)


@dataclass(slots=True, kw_only=True)
class ORMHouses:
    model: "Houses" = HouseModel
    filters: "HousesFilters" = None
    longitude: Longitude
    latitude: Latitude
    distance: float

    def filter_points_inside(self):
        point = Point(self.longitude, self.latitude)
        return self.filter(geometry__distance_lt=(point, Distance(km=self.distance)))

    def filter_quaters_inside(self) -> Union[QuerySet, List[HouseModel]]:
        return self.filter_points_inside(self).aggregate(
            quarters_count=Sum("quarters_count")
        )["quarters_count"]

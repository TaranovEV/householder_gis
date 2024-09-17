from dataclasses import dataclass, field
from typing import Union, List

from django.db.models import QuerySet

from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)
from geo_back.householder_gis.simplegis.infra.django_models.models import House
from geo_back.householder_gis.simplegis.infra.repositories.bus_stops import ORMBusStops


@dataclass(slots=True, kw_only=True)
class BusStopsService:
    longitude: Longitude
    latitude: Latitude
    distance: float
    orm_service: ORMBusStops = field(init=False)

    def __post_init__(self):
        self.orm_service = ORMBusStops(
            longitude=self.longitude, latitude=self.latitude, distance=self.distance
        )

    def get_stops_inside_circle_zone(self) -> Union[QuerySet, List[House]]:
        return self.orm_service.filter_stops_inside(
            longitude=self.longitude, latitude=self.latitude, distance=self.distance
        )

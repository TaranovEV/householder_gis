from dataclasses import dataclass, field
from typing import Union, List

from django.db.models import QuerySet

from geo_back.householder_gis.simplegis.domain.entities.isochrone import Isochrone
from geo_back.householder_gis.simplegis.infra.django_models.models import House
from geo_back.householder_gis.simplegis.infra.repositories.bus_stops import ORMBusStops


@dataclass(slots=True, kw_only=True)
class BusStopsService:
    isochrone: Isochrone
    orm_service: ORMBusStops = field(init=False)

    def __post_init__(self):
        self.orm_service = ORMBusStops(isochrone=self.isochrone)

    def get_stops_inside_circle_zone(self) -> Union[QuerySet, List[House]]:
        return self.orm_service.filter_stops_inside()

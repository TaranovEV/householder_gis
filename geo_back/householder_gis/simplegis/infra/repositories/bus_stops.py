from dataclasses import dataclass
from typing import Union, List

from django.contrib.gis.measure import Distance
from django.db.models import Count, QuerySet

from geo_back.householder_gis.simplegis.domain.entities.isochrone import Isochrone
from geo_back.householder_gis.simplegis.infra.django_models.models import (
    BusStop as BusStopsModel,
)


@dataclass(slots=True, kw_only=True)
class ORMBusStops:
    model: "BusStopsModel" = BusStopsModel
    filters: "BusStopsFilters" = None
    isochrone: Isochrone

    def filter_points_inside(self):
        return self.filter(
            geometry__distance_lt=(
                self.isochrone.center,
                Distance(km=self.isochrone.inner_radius),
            )
        )

    def filter_stops_inside(self) -> Union[QuerySet, List[BusStopsModel]]:
        routes = set()
        filtered = self.filter_points_inside()
        for stop in filtered:
            routes.update(stop.route_numbers.split(";"))
        return (
            filtered,
            filtered.aggregate(bus_stop_count=Count("name"))["bus_stop_count"],
            len(routes),
        )

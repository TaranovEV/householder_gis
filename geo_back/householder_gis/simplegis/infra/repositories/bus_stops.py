from dataclasses import dataclass
from typing import Union, List

from django.contrib.gis.measure import Distance
from django.db.models import Count, QuerySet

from geo_back.householder_gis.simplegis.domain.entities.bus_stops import BusStop
from geo_back.householder_gis.simplegis.domain.entities.isochrone import Isochrone
from geo_back.householder_gis.simplegis.infra.django_models.models import (
    BusStop as BusStopsModel,
)
from geo_back.householder_gis.simplegis.interfaces.serializers.serrializers import (
    BusStopSerializer,
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

    def to_entity(self, obj: QuerySet) -> BusStop:
        return BusStop(
            name=obj.name, route_numbers=obj.route_numbers, geometry=obj.geometry
        )

    def filter_stops_inside(self) -> Union[QuerySet, List[BusStopsModel]]:
        routes = set()
        bus_stops_data = self.filter_points_inside()

        for stop in bus_stops_data:
            routes.update(stop.route_numbers.split(";"))
        return (
            BusStopSerializer(bus_stops_data, many=True).data,
            bus_stops_data.aggregate(bus_stop_count=Count("name"))["bus_stop_count"],
            len(routes),
        )

from dataclasses import dataclass
from typing import Union, List

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.db.models import Count, QuerySet
from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)
from geo_back.householder_gis.simplegis.infra.django_models.models import (
    BusStop as BusStopsModel,
)


@dataclass(slots=True, kw_only=True)
class ORMBusStops:
    model: "BusStopsModel" = BusStopsModel
    filters: "BusStopsFilters" = None
    longitude: Longitude
    latitude: Latitude
    distance: float

    def filter_points_inside(self):
        point = Point(self.longitude, self.latitude)
        return self.filter(geometry__distance_lt=(point, Distance(km=self.distance)))

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

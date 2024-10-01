from dataclasses import dataclass

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

from geo_back.householder_gis.simplegis.domain.entities.isochrone import Isochrone
from geo_back.householder_gis.simplegis.domain.values.geometry import (
    Latitude,
    Longitude,
)
from geo_back.householder_gis.simplegis.infra.django_models.models import (
    Metro as MetroModel,
)
from geo_back.householder_gis.simplegis.interfaces.serializers.serrializers import (
    MetroStationSerializer,
)


@dataclass(slots=True, kw_only=True)
class ORMMetroStations:
    model: "Metro" = MetroModel
    filters: "MetroStationsFilters" = None
    isochrone: Isochrone

    def filter_stations_inside(self):
        point = self.isochrone.center
        stations = self.model.filter(
            geometry__distance_lt=(point, Distance(km=self.distance))
        )
        return MetroStationSerializer(stations, many=True).data

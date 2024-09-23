from dataclasses import dataclass

from geo_back.householder_gis.simplegis.domain.entities.geodata_layer import (
    GeoDataLayer,
)
from geo_back.householder_gis.simplegis.domain.entities.isochrone import Isochrone
from geo_back.householder_gis.simplegis.services.bus_stops import BusStopsService
from geo_back.householder_gis.simplegis.services.houses import HousesService
from geo_back.householder_gis.simplegis.services.isochrone import IsochronService
from geo_back.householder_gis.simplegis.services.metro_stations import (
    MetroStationsService,
)
from geo_back.householder_gis.simplegis.services.shops import ShopsService


@dataclass(slots=True, kw_only=True)
class GeoDataLayerService:
    type_iso: str
    time_iso: int
    isochrone: Isochrone

    house_service: HousesService
    shops_service: ShopsService
    bus_stops_service: BusStopsService
    metro_stations_service: MetroStationsService
    isochrone_service: IsochronService

    def init_bus_station_service(self):
        bus_stops_service = BusStopsService(isochrone=self.isochrone)
        (
            bus_stops,
            bus_stops_count,
            bus_routes_count,
        ) = bus_stops_service.get_stops_inside_circle_zone()
        return bus_stops, bus_stops_count, bus_routes_count

    def init_house_service(self):
        house_service = HousesService(
            longitude="longitude", latitude="latitude", distance="distance"
        )
        quarters_count = house_service.get_quaters_inside_circle_zone()
        return quarters_count

    def init_shops_service(self):
        shops_service = ShopsService(
            longitude="longitude", latitude="latitude", distance="distance"
        )
        our_shops = shops_service.get_our_shops_inside_circle_zone(
            longitude="longitude", latitude="latitude", distance="distance"
        )
        opponents = shops_service.get_competitor_shops_inside_circle_zone(
            longitude="longitude", latitude="latitude", distance="distance"
        )
        return our_shops, opponents

    def init_metro_stations_service(self):
        metro_stations_service = MetroStationsService(
            longitude="longitude", latitude="latitude", distance="distance"
        )
        metro_stations = metro_stations_service.get_stations_inside_circle_zone(
            longitude="longitude", latitude="latitude", distance="distance"
        )
        return metro_stations

    def build_layer(self) -> GeoDataLayer:
        bus_stops, bus_stops_count, bus_routes_count = self.init_bus_station_service()
        quarters_count = self.init_house_service()
        our_shops, opponents = self.init_shops_service()
        metro_stations = self.init_metro_stations_service()
        return GeoDataLayer(
            type_iso=self.type_iso,
            time_iso=self.time_iso,
            quarters_count=quarters_count,
            bus_station=bus_stops,
            bus_routes_count=bus_routes_count,
            bus_stop_count=bus_stops_count,
            metro_stations=metro_stations,
            opponents=opponents,
            our_shops=our_shops,
            pin_coords=[None, None],
            geometry=Isochrone,
        )

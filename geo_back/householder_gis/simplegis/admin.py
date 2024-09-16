from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from geo_back.householder_gis.simplegis.infra.django_models.models import (
    BusStop,
    House,
    Metro,
    Shop,
)


@admin.register(House)
class HouseAdmin(OSMGeoAdmin):
    pass


@admin.register(Metro)
class MetroAdmin(OSMGeoAdmin):
    pass


@admin.register(BusStop)
class BusStopAdmin(OSMGeoAdmin):
    pass


@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    pass

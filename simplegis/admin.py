from django.contrib import admin
from .models import House, Metro, BusStop, Shop
from django.contrib.gis.admin import OSMGeoAdmin


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

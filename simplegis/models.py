from django.contrib.gis.db import models
from django.contrib.gis.db.models.functions import Distance as D
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.db.models import Count, Sum
from django.db.models.functions import Round


 
def distance(self, lon, lat, dist):  
    point = Point(lon, lat)
    return self.filter(geometry__distance_lt=(point, Distance(km=dist)))


class HouseQuerySet(models.QuerySet):
    def get_quaters_in_R(self, lon, lat, dist):
        return (
            distance(self, lon, lat, dist)
            .aggregate(quarters_count = Sum('quarters_count'))
        )


class MetroQuerySet(models.QuerySet):
    def get_stations_in_R(self, lon, lat, dist):
        return (
            distance(self, lon, lat, dist)
        )


class BusStopQuerySet(models.QuerySet):
    def get_stops_in_R(self, lon, lat, dist):
        routes = set()
        filtered = (
            distance(self, lon, lat, dist)
        )
        for stop in filtered:
            routes.update(stop.route_numbers.split(';'))
        return (
            filtered,
            filtered
                .aggregate(bus_stop_count = Count('name'))['bus_stop_count'],
                len(routes)
        )


class ShopQuerySet(models.QuerySet):
    def get_shops_in_R(self, lon, lat, dist):
        point = Point(lon, lat)
        return (
            self.filter(geometry__distance_lt=(point, Distance(km=dist)))
            .annotate(distance=Round(D('geometry', point)))
        )
    
    
class House(models.Model):
    address = models.CharField(verbose_name='адрес', max_length=200,
                               blank=False, null=False)
    quarters_count = models.PositiveIntegerField(verbose_name='количество_домохозяйств',
                                                 blank=False, null=False)
    geometry = models.GeometryField()

    objects = HouseQuerySet.as_manager()
    
    
    class Meta:
        verbose_name = 'домохозяйство'
        verbose_name_plural = 'домохозяйства'
    
       
    def __str__(self):
        return self.address


class Metro(models.Model):
    name = models.CharField(verbose_name='название', max_length=200,
                            blank=False, null=False)
    line = models.CharField(verbose_name='линия_метрополитена', max_length=200,
                            blank=False, null=False)
    incoming_passengers = models.PositiveIntegerField(verbose_name='трафик пассажиров',
                                                      blank=False, null=False)
    geometry = models.GeometryField()

    objects = MetroQuerySet.as_manager()
    
    
    class Meta:
        verbose_name = 'станция метрополитена'
        verbose_name_plural = 'станции метрополитена'
       
     
    def __str__(self):
        return self.name


class BusStop(models.Model):
    name = models.CharField(verbose_name='название', max_length=100,
                            blank=False, null=False)
    route_numbers = models.CharField(verbose_name='маршруты', max_length=600,
                                     blank=False, null=False)
    geometry = models.GeometryField()

    objects = BusStopQuerySet.as_manager()
    
    
    class Meta:
        verbose_name = 'остановка ОТ'
        verbose_name_plural = 'остановки ОТ'
    
    
    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(verbose_name='название', max_length=200,
                            blank=False, null=False)
    address = models.CharField(verbose_name='адрес', max_length=200,
                               blank=False, null=False)
    square = models.FloatField(verbose_name='площадь, м2', default=0,
                               blank=False, null=False)
    sales = models.FloatField(verbose_name='оборот, в руб./мес.', default=0,
                              blank=False, null=False)
    geometry = models.GeometryField()
    
    objects = ShopQuerySet.as_manager()

    
    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'магазины'
        
        
    def __str__(self):
        return self.name

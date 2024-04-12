import random

import factory
from django.contrib.gis.geos import Point
from faker.providers import BaseProvider
from householder_gis.simplegis.models import BusStop, House, Metro, Shop


def random_coordinates():
    return (random.uniform(-180.0, 180.0), random.uniform(-180.0, 180.0))


class DjangoGeoPointProvider(BaseProvider):
    def point(self):
        return Point(random_coordinates(), random_coordinates())


factory.Faker.add_provider(DjangoGeoPointProvider)


class HouseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = House

    address = factory.Sequence(lambda n: f"Street {n}")
    quarters_count = 10.0
    geometry = factory.Faker("point")


class BusStopFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BusStop

    name = factory.Sequence(lambda n: f"BusStop {n}")
    route_numbers = 3
    geometry = factory.Faker("point")


class MetroFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Metro

    name = factory.Sequence(lambda n: f"Name {n}")
    line = factory.Sequence(lambda n: f"Line {n}")
    incoming_passengers = 1_000_000
    geometry = factory.Faker("point")


class ShopFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Shop

    name = factory.Sequence(lambda n: f"Name {n}")
    address = factory.Sequence(lambda n: f"Street {n}")
    square = 500.0
    sales = 250_000.0
    geometry = factory.Faker("point")

import pytest
from django.contrib.gis.geos import GEOSGeometry
from householder_gis.simplegis.tests.factories import (
    BusStopFactory,
    HouseFactory,
    MetroFactory,
    ShopFactory,
)


@pytest.mark.django_db
def test_create_house():
    record = HouseFactory.create()
    assert record.id is not None
    assert record.address == "Street 0"
    assert record.quarters_count == 10.0
    assert GEOSGeometry(record.geometry).geom_type == "Point"


@pytest.mark.django_db
def test_create_busstop():
    record = BusStopFactory.create()
    assert record.id is not None
    assert record.name == "BusStop 0"
    assert record.route_numbers == 3
    assert GEOSGeometry(record.geometry).geom_type == "Point"


@pytest.mark.django_db
def test_create_metrostation():
    record = MetroFactory.create()
    assert record.id is not None
    assert record.name == "Name 0"
    assert record.line == "Line 0"
    assert record.incoming_passengers == 1_000_000
    assert GEOSGeometry(record.geometry).geom_type == "Point"


@pytest.mark.django_db
def test_create_shop():
    record = ShopFactory.create()
    assert record.id is not None
    assert record.name == "Name 0"
    assert record.address == "Street 0"
    assert record.square == 500.0
    assert record.sales == 250_000.0
    assert GEOSGeometry(record.geometry).geom_type == "Point"


@pytest.mark.django_db
def test_calculate_auth_user(api_client, geo_data):
    response = api_client.get("/api/map/calculate/", data=geo_data)
    assert response.status_code == 200


@pytest.mark.django_db
def test_calculate_noauth_user(unauth_client, geo_data):
    response = unauth_client.get("/api/map/calculate/", data=geo_data)
    assert response.status_code == 401

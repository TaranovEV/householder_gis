import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def api_client() -> APIClient:
    user = User.objects.create_user(username="testuser", password="12345")
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return client


@pytest.fixture
def unauth_client():
    return APIClient()


@pytest.fixture
def geo_data():
    return {"lat": 37.529083, "lon": 55.771915, "type_iso": "auto", "time_iso": 5}

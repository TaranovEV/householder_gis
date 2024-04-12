from django.urls import include, path
from householder_gis.simplegis.views import ShowZone

from householder_gis import settings

app_name = "householder_gis.simplegis"

urlpatterns = [
    path("calculate/", ShowZone.as_view(), name="showzone"),
]


if settings.DEBUG:
    urlpatterns.append(path("__debug__", include("debug_toolbar.urls")))

from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import MapView, showzone



app_name = "householder_gis.simplegis"

urlpatterns = [
    path("map/", login_required(MapView.as_view())),
    path('<str:lat>,<str:lon>,<str:type_iso>,<str:time_iso>',
         showzone,
         name='showzone'),
]

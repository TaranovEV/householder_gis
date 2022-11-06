from django.urls import path

from .views import MapView
from .views import showzone

app_name = "gis"

urlpatterns = [
    path("map/", MapView.as_view()),
    path('<str:lat>,<str:lon>,<str:type_iso>,<str:time_iso>',
         showzone,
         name='showzone'),
]

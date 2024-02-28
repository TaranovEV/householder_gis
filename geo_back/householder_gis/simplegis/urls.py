from django.contrib.auth.decorators import login_required
from django.urls import path, include

from householder_gis import settings
# from .views import MapView, showzone
from householder_gis.simplegis.views import ShowZone


app_name = "householder_gis.simplegis"

urlpatterns = [
    # path("/init/", login_required(MapView.as_view())),
    path('calc/', ShowZone.as_view(), name='showzone'),
]


if settings.DEBUG:
    urlpatterns.append(
        path('__debug__', include('debug_toolbar.urls'))
    )

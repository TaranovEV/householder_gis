from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from householder_gis.simplegis.urls import urlpatterns as api_v1

schema_view = get_schema_view(
    openapi.Info(title='SIMPLE GIS', default_version='v2', description='API docs'),
    url='http://127.0.0.1:8000/api',
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = ([
    re_path(r'^admin/', admin.site.urls),
    re_path(r"^api/map/", include("householder_gis.simplegis.urls")),
]
+ static(settings.STATIC_URL)
)

urlpatterns += [
    re_path(r'^api/swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

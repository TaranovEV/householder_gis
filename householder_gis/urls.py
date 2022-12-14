from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("simplegis/", include("simplegis.urls")),
]
+ static(settings.STATIC_URL)
)

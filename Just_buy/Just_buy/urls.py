
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/auth2/',include('djoser.urls')),
    re_path(r'^auth2/',include('djoser.urls.authtoken')),
]

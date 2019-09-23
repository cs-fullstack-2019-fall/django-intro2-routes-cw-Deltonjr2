from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("endpoint66_app.urls")),
    path('admin/', admin.site.urls),
]






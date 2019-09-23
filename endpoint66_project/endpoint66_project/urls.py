from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('endpoint66/', include("endpoint66_app.urls")),
    path('admin/', admin.site.urls),
]
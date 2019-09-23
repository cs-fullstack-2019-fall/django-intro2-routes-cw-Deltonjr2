from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('endpoint66/', include('route66.urls')),
    path('admin/', admin.site.urls),
]






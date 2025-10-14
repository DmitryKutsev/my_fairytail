"""URL configuration for My Fairy Tale project."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("stories.urls")),
]

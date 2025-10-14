from django.urls import path

from .views import FairyTaleSearchView

app_name = "stories"

urlpatterns = [
    path("", FairyTaleSearchView.as_view(), name="search"),
]

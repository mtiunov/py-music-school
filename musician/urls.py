from django.urls import path, include
from rest_framework import routers
from .views import MusicianViewSet

app_name = "musician"

router = routers.DefaultRouter()
router.register("musicians", MusicianViewSet, basename="manage")


urlpatterns = [
    path("", include(router.urls)),
]

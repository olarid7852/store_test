from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import viewsets


router = DefaultRouter()
router.register('', viewsets.StoreViewSet, basename="store")

urlpatterns = [
    path('', include(router.urls)),
]

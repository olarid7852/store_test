from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import viewsets


router = DefaultRouter()
router.register('', viewsets.OrderViewSet, basename="order")

order_router = DefaultRouter()
order_router.register('item', viewsets.OrderItemViewSet, basename="item")

urlpatterns = [
    path('', include(router.urls)),
    path('<int:order_id>/', include(order_router.urls)),
]

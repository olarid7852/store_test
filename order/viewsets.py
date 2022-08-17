from rest_framework.decorators import action
from rest_framework import response, viewsets

from . import models
from . import serializers


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        queryset = models.Order.objects.all()
        params = self.request.query_params
        store_id = params.get('store_id')
        if store_id:
            queryset = queryset.filter(store_id=store_id)
        return queryset

class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderItemSerializer

    def get_queryset(self):
        return models.OrderItem.objects.filter(order_id=self.kwargs['order_id'])

    def perform_create(self, serializer):
        return serializer.save(order_id=self.kwargs['order_id'])

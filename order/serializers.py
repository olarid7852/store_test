from rest_framework import serializers

from . import models


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        exclude = ('deleted_at',)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        exclude = ('deleted_at',)
        read_only_fields = ('order',)

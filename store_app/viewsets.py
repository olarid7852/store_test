from rest_framework.decorators import action
from rest_framework import response, viewsets

from . import models
from . import serializers


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StoreSerializer

    def get_queryset(self):
        return models.Store.objects.all()

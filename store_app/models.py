from django.db import models

from core.models import SoftDeleteModel


class Store(SoftDeleteModel):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

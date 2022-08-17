from django.db import models

from core.models import SoftDeleteModel
from store_app.models import Store


class Order(SoftDeleteModel):
    class OrderStatus(models.TextChoices):
        opened = "OP"
        cancelled = "CA"
        delivered = "DA"

    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    status = models.CharField(max_length=2, choices=OrderStatus.choices, null=True, blank=True)
    opened_time = models.DateTimeField(auto_now_add=True)


class OrderItem(SoftDeleteModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

from django.contrib import admin

from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, *args) -> bool:
        if len(args) > 0:
            return args[0].status != Order.OrderStatus.cancelled
        return True

admin.site.register(Order, OrderAdmin)

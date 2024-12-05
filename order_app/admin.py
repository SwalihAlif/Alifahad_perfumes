from django.contrib import admin
from .models import Order, OrderItems, Cancelled_order

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(Cancelled_order)

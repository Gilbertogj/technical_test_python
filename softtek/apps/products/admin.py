from django.contrib import admin
from apps.products.models import OrderLine, Order

# Register your models here.

admin.site.register(OrderLine)
admin.site.register(Order)
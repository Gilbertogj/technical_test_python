from django.contrib import admin
from apps.products.models import OrderLine, Order
from apps.seasons.models import CustomerOrder

# Register your models here.

admin.site.register(OrderLine)
admin.site.register(Order)
admin.site. register(CustomerOrder)
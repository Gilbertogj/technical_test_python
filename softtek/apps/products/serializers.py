from rest_framework import serializers
from app.products.models import OrderLine

class OrdersLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = '__all__'
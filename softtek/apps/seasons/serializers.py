from rest_framework import serializers
from apps.seasons.models import CustomerOrder

class CustomerOrdersSerializer(serializers.ModelSerializer):
    lines = serializers.SerializerMethodField(
        read_only=True, method_name="season_status"
    )
    
    class Meta:
        model = CustomerOrder
        fields = "__all__"
    
    def season_status(self, instance):
        "Returns the person's baby-boomer status."
        import datetime
        if instance.order_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif instance.order_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"
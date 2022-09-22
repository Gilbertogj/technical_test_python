from rest_framework import serializers
from apps.seasons.models import CustomerOrder
from datetime import date, datetime

class CustomerOrdersSerializer(serializers.ModelSerializer):
    season = serializers.SerializerMethodField(
        read_only=True, method_name="season_status"
    )
    
    class Meta:
        model = CustomerOrder
        fields = "__all__"

    
    def season_status(self, instance):
        "Returns the season"
        print(type(instance.order_date))
        year=int(instance.order_date.strftime("%Y"))
        print(type(year))

        import datetime
        if datetime.date(year, 3, 19) <= instance.order_date <= datetime.date(year, 6, 19):
            return "Spring"
        elif datetime.date(year, 6, 20) <= instance.order_date <= datetime.date(year, 9, 21):
            return "Summer"
        elif datetime.date(year, 9, 22) <= instance.order_date <= datetime.date(year, 12, 20):
            return "Fall"
        else:
            return "Winter"
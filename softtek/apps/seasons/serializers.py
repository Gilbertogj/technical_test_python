from rest_framework import serializers
from apps.seasons.models import CustomerOrder
from datetime import date, datetime

class CustomerOrdersSerializer(serializers.ModelSerializer):
    lines = serializers.SerializerMethodField(
        read_only=True, method_name="season_status"
    )
    
    class Meta:
        model = CustomerOrder
        fields = "__all__"
    

    # Y = 2000
    # seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
    #            ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
    #            ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
    #            ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
    #            ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]

    # def get_season(self, instance):
    #     if isinstance(now, datetime):
    #         now = instance.order_date.date()
    #     now = now.replace(year=Y)
    #     return next(season for season, (start, end) in seasons if start <= now <= end)

    # print(get_season(date.today()))

    
    def season_status(self, instance):
        "Returns the person's baby-boomer status."
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
from rest_framework import serializers
from apps.weather.models import Weather
from datetime import date, datetime

class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = "__all__"
    
    
    

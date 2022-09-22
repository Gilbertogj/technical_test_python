from django.shortcuts import render
from rest_framework import generics
from .serializers import WeatherSerializer
from .models import Weather


# Create your views here.

class ListWeatherApiView(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        
        queryset = Weather.objects.all()
        response=[]
        refference= True

        for key in queryset.values():
            if (key["rain"]) == True and refference == True:
                response.append(key)
                refference = False
            elif (key["rain"]) == False:
                refference = True
        print (response)


        return response



class CreateWeatherApiView(generics.CreateAPIView):
    serializer_class = WeatherSerializer
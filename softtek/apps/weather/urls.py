from django.urls import path 

from apps.weather.views import ListWeatherApiView, CreateWeatherApiView 

urlpatterns =[

    path('weather-table/list/', ListWeatherApiView.as_view(), name = 'list-weather' ),
    path('weather/create/', CreateWeatherApiView.as_view(), name = 'create-weather' ),
    

]
from django.shortcuts import render
from rest_framework import generics
from .serializers import OrderSerializer, OrderLinesSerializer
from .models import Order, OrderLine

# Create your views here.

class ListOrderApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class CreateOrderApiView(generics.CreateAPIView):
    serializer_class = OrderSerializer

class CreateOrderLineApiView(generics.CreateAPIView):
    serializer_class = OrderLinesSerializer

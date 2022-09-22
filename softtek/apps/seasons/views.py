from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomerOrdersSerializer
from .models import CustomerOrder


# Create your views here.

class ListCustomerOrderApiView(generics.ListAPIView):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrdersSerializer

class CreateCustomerOrderApiView(generics.CreateAPIView):
    serializer_class = CustomerOrdersSerializer

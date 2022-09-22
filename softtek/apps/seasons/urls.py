from django.urls import path 

from apps.seasons.views import ListCustomerOrderApiView, CreateCustomerOrderApiView 

urlpatterns =[

    path('customer-orders/list/', ListCustomerOrderApiView.as_view(), name = 'list-customer-orders' ),
    path('customer-orders/create/', CreateCustomerOrderApiView.as_view(), name = 'create-customer-orders' ),
    

]
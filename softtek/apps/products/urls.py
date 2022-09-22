from django.urls import path 

from apps.products.views import CreateOrderApiView, CreateOrderLineApiView, ListOrderApiView

urlpatterns =[

    path('orders/list/', ListOrderApiView.as_view(), name = 'list-orders' ),
    path('orders/create/', CreateOrderApiView.as_view(), name = 'create-orders' ),
    path('orders-lines/create/', CreateOrderLineApiView.as_view(), name = 'create-orders-lines' ),

]
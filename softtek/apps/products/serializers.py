from rest_framework import serializers
from apps.products.models import Order, OrderLine


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'


    order_status = serializers.SerializerMethodField(
            read_only=True, method_name="get_status"
        )
    #Method to obtain order status 

    def get_status(self, instance):
        response = OrderLine.objects.filter(order_id=instance.id)
        
        dict_response= response.values()

        for key in dict_response: 
            if (key["status"]) == "PENDING":
                status = "PENDING"
                break
            elif (key["status"]) == "SHIPPED":
                status = "SHIPPED"
                
            else:
                status = "CANCELLED"
            
        return status

class OrderLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = "__all__"
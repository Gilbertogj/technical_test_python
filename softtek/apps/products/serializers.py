from rest_framework import serializers
from apps.products.models import Order, OrderLine


class OrderSerializer(serializers.ModelSerializer):
    
    lines = serializers.SerializerMethodField(
        read_only=True, method_name="get_lines"
    )
    
    # stat= serializers.SerializerMethodField(
    #     read_only=True, method_name="v_lines"
    # )

    class Meta:
        model = Order
        fields = '__all__'
    
    def get_lines(self, instance):

        response = OrderLine.objects.filter(order_id=instance.id)

        response = OrderLinesSerializer(response, context=self.context, many=True)


        return response.data
    
    # def v_lines(self, instance):

    #     #lineas = self.request.data["lines"]

    #     for linea in instance.lines:
    #         if linea["status"] == "PENDING":
    #             validaciones = "PENDING"
    #         else:
    #             validaciones = "SHIPPED"

    #     validaciones.is_valid(raise_exception=True)

    #     return validaciones

class OrderLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = ("status",)
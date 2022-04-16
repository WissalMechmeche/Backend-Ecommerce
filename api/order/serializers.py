from api.orderItem.serializers import OrderItemSerializer
from api.customer.serializers import CustomerSerializer
from rest_framework import serializers
from .models import Order 


class OrderSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField(read_only=True)
    
    class Meta :
        model = Order
        fields = ('__all__')
        
    def get_orderItems(self, obj):
        items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data
    def get_customer(self, obj):
        query = obj.customer_set.all()
        serializer = CustomerSerializer(query, many=True)
        return serializer.data
     
      
   
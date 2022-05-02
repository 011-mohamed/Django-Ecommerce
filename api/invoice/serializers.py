from api.customer.models import Customer
from api.customer.serializers import CustomerSerializer
from api.orderItem.serializers import OrderItemSerializer
from rest_framework import serializers
from api.invoice.models import Invoice
from api.order.serializers import OrderSerializer

class InvoiceSerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField(read_only=True)
    items = serializers.SerializerMethodField(read_only=True)
    class Meta :
        model = Invoice
        fields = ('__all__')
        
    def get_order(self, obj):
        order = obj.order
        serializer = OrderSerializer(order, many=False)
        return serializer.data
    def get_items(self , obj):
        items = obj.order.orderitem_set.all()
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data
    
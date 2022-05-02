from api.orderItem.models import OrderItem
from api.orderItem.serializers import OrderItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.



@api_view(['GET'])
def getOrderItems(request):
        
    queryset = OrderItem.objects.all()
    serailizer = OrderItemSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )

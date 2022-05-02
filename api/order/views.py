
from asyncio.windows_events import NULL
from dataclasses import dataclass
from pickle import NONE
import this
from webbrowser import get


from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

from api.customer.serializers import CustomerSerializer
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.product.models import Product
from api.order.models import Order
from api.orderItem.models import OrderItem
from api.customer.models import Customer
from api.purchase.models import Purchase


# Create your views here.


@api_view(['POST','GET'])
@parser_classes([JSONParser])
def addOrderItems(request):
    
    data = request.data
    customer = NULL 
    
    
    #c = purchase['customer']
    orderItems = data.get("orderItems")
    c = data.get("customer")
    o = data.get("order")
    tel = c.get("phoneNumber")
    fn =c.get("firstName")
    ln =  c.get("lastName")
    cp = c.get("company")

    
    
     
    
    if orderItems and len(orderItems) == 0:
        return Response({'detail': 'No Order Items'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        query = Customer.objects.filter(phoneNumber=tel)
        serailizer = CustomerSerializer(query , many=True)
        customerFromDB = serailizer.data
        
        if(customerFromDB != NULL):
           
            for i in customerFromDB:
                customer = Customer.objects.get(phoneNumber=i['phoneNumber'])
                break
        if(customer == NULL):
            
            customer = Customer.objects.create(
                firstName =fn,
                lastName =ln,
                phoneNumber = tel,
                company = cp  )     
                    
        # (2) Create order
        order = Order.objects.create(
            totalPrice=o.get("totalPrice"),
            totalQuantity=o.get("totalQuantity"),
            customer_Or = customer
        )
        
        

        # (3) Create order items adn set order to orderItem relationship
        for i in orderItems:
            product = Product.objects.get(id=i['product'])

            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                qty=i['qty'],
                price=i['price'],
                
            )

            # (4) Update stock

            product.unitStock -= item.qty
            product.save()

        serializer = OrderSerializer(order, many=False)
        return Response(serializer.data)

@api_view(['GET'])
def getOrders(request):
        
    queryset = Order.objects.all()
    serailizer = OrderSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )

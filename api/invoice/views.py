from asyncio.windows_events import NULL
from api.invoice.models import Invoice
from api.invoice.serializers import InvoiceSerializer
from api.order.models import Order
from api.customer.models import Customer
from api.customer.serializers import CustomerSerializer
from api.order.serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

# Create your views here.
@api_view(['POST'])
@parser_classes([JSONParser])
def addBill(request):
    
    data = request.data
    billid = data.get("billId")
    o = data.get("order")
    customer = data.get("customer")
    tel = customer.get("phoneNumber")
    tn = data.get("orderTN")
    orderFDB = NULL 
    
    query = Customer.objects.filter(phoneNumber=tel)
    serailizer = CustomerSerializer(query , many=True)
    customerFromDB = serailizer.data
    
    queryO= Order.objects.filter(orderTrackingNumber=tn)
    serailiz = OrderSerializer(queryO , many=True)
    orderFromDB = serailiz.data
    
    
    if(customerFromDB != NULL):
           
        for i in customerFromDB:
            customer = Customer.objects.get(phoneNumber=i['phoneNumber'])
            break
        
    
    if(orderFromDB != NULL):      
        for i in orderFromDB:
            orderFDB = Order.objects.get(orderTrackingNumber=i['orderTrackingNumber'])
            break
    
    if(orderFDB == NULL):
        orderFDB = Order.objects.create(
            orderTrackingNumber = o.get("orderTrackingNumber"),
            totalPrice=o.get("totalPrice"),
            totalQuantity=o.get("totalQuantity"),
            customer_Or = customer
        )
   
        
    bill = Invoice.objects.create(
        billId = billid,
        order = orderFDB
        
    )
    serializer = InvoiceSerializer(bill, many=False)
    
    return Response(serializer.data)


@api_view(['GET'])
def getBills(request):
        
    queryset = Invoice.objects.all()
    serailizer = InvoiceSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )

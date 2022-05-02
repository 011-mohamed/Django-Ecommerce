from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.customer.models import Customer
from api.customer.serializers import CustomerSerializer

# Create your views here.

@api_view(['GET'])
def getCustomers(request):
        
    queryset = Customer.objects.all()
    serailizer = CustomerSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )

@api_view(['GET'])
def getCustomer(request, pk):
    queryset = Customer.objects.get(id=pk)
    serailizer = CustomerSerializer(queryset, many=False, context={"request": request})
    return Response(serailizer.data )


@api_view(['GET'])
def getCustomersByPhoneNumber(request ,  tel):
    query = Customer.objects.filter(phoneNumber=tel)
    serailizer = CustomerSerializer(query , many=True)
    return Response(serailizer.data )

@api_view(['POST'])
def createCustomer(request):
    data = request.data
    
    customer = Customer.objects.create(
        firstName=data['firstName'],
        lastName=data['lastName'],
        phoneNumber=data['phoneNumber'],
        company=data['company']
        
    )
    
    serailizer = CustomerSerializer(customer , many=False)
       
    return Response(serailizer.data )

@api_view(['DELETE','GET'])
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return Response('Customer Deleted' )


@api_view(['PUT','GET'])
def updateCustomer(request, pk):
    data = request.data
    customer = Customer.objects.get(id=pk)
    
    customer.firstName=data['firstName']
    customer.lastName=data['lastName']
    customer.phoneNumber=data['phoneNumber']
    customer.company=data['company']
    
    
    customer.save()
    
    
    serailizer = CustomerSerializer(customer, many=False)
    return Response(serailizer.data )
from rest_framework.response import Response
from rest_framework.decorators import api_view
from asyncio.windows_events import NULL
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
    query = Customer.objects.get(phoneNumber=tel)
    serailizer = CustomerSerializer(query , many=False)
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


@api_view(['GET'])
def getCustomersFiltredByName(request, keyword):
    if keyword == None: 
        keyword = ''
    
    queryset = Customer.objects.filter(firstName__icontains=keyword)
    serailizer = CustomerSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )

@api_view(['GET'])
def getCustomersFiltredByPhoneNumber(request, keyword):
    if keyword == None: 
        keyword = NULL
    
    queryset = Customer.objects.filter(phoneNumber__icontains=keyword)
    serailizer = CustomerSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )


@api_view(['GET'])
def getCustomersOrderByDate(request):
        
    queryset = Customer.objects.order_by('-created_at')
    serailizer = CustomerSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )



@api_view(['GET'])
def getCountOfCustomers(request):
        
    queryset = Customer.objects.all().count()
    context= {'count': queryset}
       
    return Response(context )


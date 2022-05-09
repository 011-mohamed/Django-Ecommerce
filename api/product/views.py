from itertools import product
from math import prod
from unicodedata import category
from api.category.models import Category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer
from api.category import models


# Create your views here.
#class ProductViewSet(viewsets.ModelViewSet):
#    queryset = Product.objects.all().order_by('id')
#    serializer_class = ProductSerializer



@api_view(['GET'])
def getProducts(request):
        
    queryset = Product.objects.all()
    serailizer = ProductSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )

@api_view(['GET'])
def getProductsFiltred(request, keyword):
    if keyword == None: 
        keyword = ''
    
    queryset = Product.objects.filter(name__icontains=keyword)
    serailizer = ProductSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )


@api_view(['GET'])
def getProductByCategory(request, ck):
    productsCat = Product.objects.filter(category=ck)
    serailizer = ProductSerializer(productsCat , many=True, context={"request": request})
    return Response(serailizer.data )
    


@api_view(['GET','PUT'])
def getProduct(request, pk):
    queryset = Product.objects.get(id=pk)
    serailizer = ProductSerializer(queryset, many=False, context={"request": request})
    return Response(serailizer.data )


@api_view(['DELETE','GET'])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Product Deleted' )


@api_view(['PUT'])
def updateProduct(request, ck):
    data = request.data
    
    product = Product.objects.get(id=ck)
    category = Category.objects.get(id=data.get("categorie"))
    
    product.name = data['name']
    product.unitPrice = data['unitPrice']
    product.unitStock = data['unitStock']
    product.category = category
    product.image = data['image']
    
    product.save()
    
    
    serailizer = ProductSerializer(product, many=False)
    return Response(serailizer.data )


@api_view(['POST'])
def addProduct(request):
    data = request.data
    cat = Category.objects.get(id=data.get("categorie"))
    
    product = Product.objects.create(
        name=data['name'],
        description=data['description'],
        unitPrice = data['unitPrice'],
        unitStock =data['unitStock'],
        image = data['image'],
        category = cat
    )
    
    serailizer = ProductSerializer(product , many=False)
       
    return Response(serailizer.data )






    
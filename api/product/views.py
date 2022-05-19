from base64 import b64encode
from django.core import serializers
from django.http import JsonResponse
from api.category.models import Category
from api.purchase.models import Result
from api.purchase.serializers import ResultSerilazer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from django.forms.models import model_to_dict


import requests
import json


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




@api_view(['GET'])
def getProductsOrderByDate(request):
        
    queryset = Product.objects.order_by('-created_at')
    serailizer = ProductSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )




@api_view(['POST','GET'])
def addProductByNyckel(request):
    data = request.data
    image = data['image']
    url = 'https://www.nyckel.com/v1/functions/7aaigszss2ejx7t8/invoke'
    header = {
    'Content-type': 'application/json', 'Accept': 'text/plain'
    }
    
    urlimg = 'http://127.0.0.1:8000/media/images/chamia_2lJVXBC.jpg'
   

    img = requests.get(urlimg,params=request.GET)
    m = img.content
    #with open('media/images/chamia_2lJVXBC.jpg', 'rb') as f:
        #result = requests.post(url, headers=header, files={'data': f})
    result = requests.post(url,m, headers=header)
    
    #dt = result.content
    #json_data = json.loads(result.text)
    
   
    
    dict = result.json() 
    
    labelName= dict.get("labelName"),
    labelId = dict.get("labelId"),
    confidence = dict.get("confidence")
    
    return Response(dict )
    
   
    
    
    





    
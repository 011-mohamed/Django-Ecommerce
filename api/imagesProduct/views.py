from django.shortcuts import render
from api.imagesProduct.models import ImagesProduct
from .serializers import ImagesProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def getImagesProduct(request):
        
    queryset = ImagesProduct.objects.all()
    serailizer = ImagesProductSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )


@api_view(['GET'])
def getImagesProductById(request,ck):
        
    queryset = ImagesProduct.objects.filter(product=ck)
    serailizer = ImagesProductSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )



@api_view(['GET'])
def getIdProductByRef(request,ref):
        
    queryset = ImagesProduct.objects.filter(reference=ref)
    serailizer = ImagesProductSerializer(queryset , many=True, context={"request": request})
       
    return Response(serailizer.data )


from datetime import date
from unicodedata import category
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializers import CategorySerializer


# Create your views here.

#class CategoryViewSet(viewsets.ModelViewSet):
#    queryset = Category.objects.all().order_by('name')
#   serializer_class = CategorySerializer


@api_view(['GET'])
def getCategory(request):
    queryset = Category.objects.all()
    serailizer = CategorySerializer(queryset , many=True)
       
    return Response(serailizer.data )

@api_view(['GET'])
def getCat(request, pk):
    queryset = Category.objects.get(id=pk)
    serailizer = CategorySerializer(queryset, many=False, context={"request": request})
    return Response(serailizer.data )


@api_view(['POST'])
def createCategory(request):
    data = request.data
    
    category = Category.objects.create(
        name=data['name'],
        description=data['description']
        
    )
    
    serailizer = CategorySerializer(category , many=False)
       
    return Response(serailizer.data )





@api_view(['DELETE','GET'])
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response('Category Deleted' )



@api_view(['PUT','GET'])
def updateCategory(request, pk):
    data = request.data
    category = Category.objects.get(id=pk)
    
    category.name = data['name']
    category.description = data['description']
    
    
    category.save()
    
    
    serailizer = CategorySerializer(category, many=False)
    return Response(serailizer.data )


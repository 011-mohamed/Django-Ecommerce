from rest_framework import serializers
from .models import Product 


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    
    class Meta :
        model = Product
        fields = ('id','image','description','name','unitPrice','unitStock','category','created_at','updated_at','is_active')



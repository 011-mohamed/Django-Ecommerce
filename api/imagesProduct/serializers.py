from dataclasses import fields
from pyexpat import model

from api.product.serializers import ProductSerializer
from .models import ImagesProduct
from rest_framework import serializers


class ImagesProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    product = serializers.SerializerMethodField(read_only=True)
    class Meta : 
        model = ImagesProduct
        fields = ('__all__')
    
    def get_product(self, obj):
        items = obj.product
        serializer = ProductSerializer(items, many=False)
        return serializer.data
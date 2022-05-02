from dataclasses import field
from rest_framework import serializers
from .models import Category 
from dataclasses import field

class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = '__all__'
        
 
from distutils.command.upload import upload
from pydoc import describe
from unicodedata import category
from django.db import models
from api.category.models import Category

# Create your models here.

class Product (models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    unitPrice = models.DecimalField(max_digits=7, decimal_places=3)
    unitStock = models.IntegerField(null= True, blank=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
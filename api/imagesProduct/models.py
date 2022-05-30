from itertools import product
from django.db import models

from api.product.models import Product

# Create your models here.
class ImagesProduct(models.Model):
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.product)
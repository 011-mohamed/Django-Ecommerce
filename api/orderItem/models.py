from django.db import models
from api.product.models import Product
from api.order.models import Order
# Create your models here.

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=3, null=True, blank=True)
    
    

    def __str__(self) -> str:
        return self.name
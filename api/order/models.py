from django.db import models
from django.db.models.signals import pre_save

from api.customer.models import Customer



from .utils import unique_order_id_generator

# Create your models here.

class Order(models.Model):
    
    orderTrackingNumber= models.CharField(max_length=120, blank= True)
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=3, null=True, blank=True)
    totalQuantity = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    customer_Or = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    

    def __str__(self):
        return str(self.orderTrackingNumber)


def pre_save_create_orderTrackingNumber(sender, instance, *args, **kwargs):
    if not instance.orderTrackingNumber:
        instance.orderTrackingNumber= unique_order_id_generator(instance)


pre_save.connect(pre_save_create_orderTrackingNumber, sender=Order)

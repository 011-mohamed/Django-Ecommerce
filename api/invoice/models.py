from django.db import models
from api.order.models import Order

# Create your models here.

class Invoice (models.Model):
    
    billId = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    customerFirstName = models.CharField(max_length=50,blank=True, null=True) 
    customerLastName = models.CharField(max_length=50,blank=True, null=True) 
    customerPhoneNumber = models.IntegerField(null= True, blank=True) 
    order = models.OneToOneField(Order,on_delete=models.CASCADE,primary_key=True)
    totalPrice = models.DecimalField(
        max_digits=12, decimal_places=3, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.billId 

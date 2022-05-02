from django.db import models
from api.order.models import Order

# Create your models here.

class Invoice (models.Model):
    billId = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    order = models.OneToOneField(Order,on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self) -> str:
        return self.billId 

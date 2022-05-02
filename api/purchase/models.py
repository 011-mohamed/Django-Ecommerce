from django.db import models

from api.customer.models import Customer
from api.order.models import Order
from api.orderItem.models import OrderItem

# Create your models here.
class Purchase (models.Model):
    customer : Customer
    order : Order
    orderItems  : OrderItem = [] 
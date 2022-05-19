from django.db import models


# Create your models here.
class Result (models.Model):
    labelName = models.CharField(max_length=120, blank= True),
    labelId = models.CharField(max_length=120, blank= True),
    confidence  = models.DecimalField(
        max_digits=7, decimal_places=3, null=True, blank=True),
    labelConfidences =  models.CharField(max_length=120, blank= True)
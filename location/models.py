from django.contrib.postgres.fields import ArrayField
from django.db import models

from farm.models import Farm

# Create your models here.
 
class Location(models.Model):
    farm=models.ForeignKey(Farm , on_delete=models.CASCADE)
    longitude=models.DecimalField(max_digits=22, decimal_places=20)
    latitude=models.DecimalField(max_digits=22, decimal_places=20)
    
def __str__(self):
     return self.lon
from django.db import models

from farm.models import Farm

# Create your models here.
 
class Machine(models.Model):
    farm=models.ForeignKey(Farm , on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    description=models.TextField()

    def __str__(self):
     return self.name

# Create your models here.
from django.db import models

from farm.models import Farm

# Create your models here.
 
class Worker(models.Model):
    farm=models.ForeignKey(Farm , on_delete=models.CASCADE)
    firstName=models.TextField()
    secondName=models.TextField()
    code=models.TextField()
    startWork=models.DateTimeField()
    workField=models.CharField(max_length=251)


    def __str__(self):
     return self.firstName
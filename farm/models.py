from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import ExtendUser
# Create your models here.

class Farm(models.Model):
    owner=models.ForeignKey(ExtendUser, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    description=models.TextField()
    culture=models.CharField(max_length=251 ,default='nothing')
    work =ArrayField(models.CharField(max_length=200), blank=True , default=list)
    token=models.CharField(max_length=650)


    def __str__(self):
     return self.name




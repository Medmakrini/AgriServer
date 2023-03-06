from django.db import models

# Create your models here.
 
from worker.models import Worker

class PresenceDate(models.Model):
    worker=models.ForeignKey(Worker , on_delete=models.CASCADE)
    date=models.DateTimeField()
    hoursofWork=models.TextField()

    def __str__(self):
     return self.hoursofWork
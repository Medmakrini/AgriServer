from django.db import models

# Create your models here.
from users.models import ExtendUser


class TodoList(models.Model):
    user=models.ForeignKey(ExtendUser , on_delete=models.CASCADE)
    date=models.DateTimeField()
    name=models.TextField()
    description=models.TextField()
    isdone=models.BooleanField(default=False)

    def __str__(self):
     return self.name
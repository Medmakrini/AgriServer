from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class ExtendUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    phone = models.TextField(blank=False, max_length=255, verbose_name="phone")
    firstName = models.TextField(blank=False, max_length=255, verbose_name="firstName")
    lastName = models.TextField(blank=False, max_length=255, verbose_name="lastName")
    code=models.TextField()
    isCodeVerified=models.BooleanField(default=False)

    def __str__(self):
     return self.firstName
    
    


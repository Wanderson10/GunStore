from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.IntegerField()
    cpf = models.CharField(max_length=14)
    is_employee = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=False )
    
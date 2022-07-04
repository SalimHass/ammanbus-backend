from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    first_name = models.CharField(max_length=80,null=True)
    last_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    user_type=models.CharField(max_length=80)




class Passenger(models.Model):
    # passenger personal information
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)

    
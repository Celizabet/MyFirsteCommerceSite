from django.db import models
from django.dispatch import receiver
from datetime import date

# Modelo de registro del Usuario - Cliente
class UserClientModel(models.Model):
    class GenderSelector(models.TextChoices):
        FEMALE = 'f', 'FEMALE'
        MALE = 'm', 'MALE'
        RATHER_NOT_SAYING = 'rns', 'RATHER NOT SAYNING'

    id = models.AutoField(primary_key=True)      
    first_name = models.CharField(max_length=100, blank=False, default=None)
    last_name = models.CharField(max_length=100, blank=False, default=None)
    username = models.CharField(max_length=50, blank=False, default=None)
    email = models.EmailField(max_length=100, unique=True, blank=False, default=None)
    password = models.CharField(max_length=50, blank=False, default=None)
    birthdate = models.DateField(max_length=10, blank=False, default=date.today)
    gender = models.CharField(
        max_length=3, 
        blank=False, 
        choices=GenderSelector.choices,
        default=GenderSelector.RATHER_NOT_SAYING)
    phone_number = models.CharField(max_length=10, blank=True, null=True, default=None)

    USERNAME_FIELD = "email"
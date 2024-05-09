from django.db import models
from clients.models import Client

# Create your models here.
class Carreto(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
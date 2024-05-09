from django.db import models
from carreto.models import Carreto

# Create your models here.
class Ordre(models.Model):
    carreto = models.OneToOneField(Carreto, on_delete=models.CASCADE)
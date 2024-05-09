from django.db import models
from comandes.models import Ordre

# Create your models here.

class Pagament(models.Model):
    ordre = models.OneToOneField(Ordre, on_delete=models.CASCADE)
    pagat = models.BooleanField(default=False)

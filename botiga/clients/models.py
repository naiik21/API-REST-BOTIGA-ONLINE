from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

class Producte(models.Model):
    nom = models.CharField(max_length=100)
    descripcio = models.TextField()
    unitats = models.IntegerField()
    estaActiu = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)

class Client(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Recuerda usar técnicas de almacenamiento seguro de contraseñas, como hash.

class Carreto(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class LlistaProductes(models.Model):
    carreto = models.ForeignKey(Carreto, on_delete=models.CASCADE)
    producte = models.ForeignKey(Producte, on_delete=models.CASCADE)
    quantitat = models.IntegerField()

class Ordre(models.Model):
    carreto = models.OneToOneField(Carreto, on_delete=models.CASCADE)

class Pagament(models.Model):
    ordre = models.OneToOneField(Ordre, on_delete=models.CASCADE)
    pagat = models.BooleanField(default=False)

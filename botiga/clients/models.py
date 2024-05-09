from django.db import models
from django.utils import timezone


class Client(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Recuerda usar técnicas de almacenamiento seguro de contraseñas, como hash.
    
    def __str__(self):
        return self.nom



    





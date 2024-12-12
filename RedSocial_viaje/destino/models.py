from django.db import models

# Create your models here.
class Destino(models.Model):
    pais = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.ciudad}, {self.pais}"
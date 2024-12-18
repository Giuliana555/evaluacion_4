from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)

    # Modificar campo de autenticación predeterminado (usar correo)
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['username', 'nombre']

    def __str__(self):
        return f"{self.correo}"

from django.db import models
from usuario.models import Usuario
from destino.models import Destino

# Create your models here.


class Publicacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Publicación de {self.usuario.nombre} sobre {self.destino.ciudad}"

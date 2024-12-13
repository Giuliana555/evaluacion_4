from rest_framework import serializers
from publicacion.models import Publicacion
from usuario.serializers import UsuarioSerializer
from destino.serializers import DestinoSerializer

class PublicacionSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)  # Datos anidados de solo lectura para Usuario
    destino = DestinoSerializer(read_only=True)  # Datos anidados de solo lectura para Destino

    class Meta:
        model = Publicacion
        fields = ['id', 'usuario', 'destino', 'texto', 'fecha']


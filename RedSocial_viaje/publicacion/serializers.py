from rest_framework import serializers
from publicacion.models import Publicacion
from usuario.serializers import UsuarioSerializer
from destino.serializers import DestinoSerializer

class PublicacionSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    destino = DestinoSerializer(read_only=True)

    class Meta:
        model = Publicacion
        fields = ['id', 'usuario', 'destino', 'texto', 'fecha']


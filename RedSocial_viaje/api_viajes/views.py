from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from destino.models import Destino
from .serializers import DestinoSerializer, PublicacionSerializer
from publicacion.models import Publicacion

@api_view(['GET'])
def listar_destinos(request):
    destinos = Destino.objects.all()
    serializer = DestinoSerializer(destinos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def filtrar_publicaciones(request):
    usuario_id = request.query_params.get('usuario', None)
    destino_id = request.query_params.get('destino', None)

    publicaciones = Publicacion.objects.all()

    if usuario_id:
        publicaciones = publicaciones.filter(usuario__id=usuario_id)
    if destino_id:
        publicaciones = publicaciones.filter(destino__id=destino_id)

    serializer = PublicacionSerializer(publicaciones, many=True)
    return Response(serializer.data)

# Create your views here.

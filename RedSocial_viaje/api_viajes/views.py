from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from destino.models import Destino
from .serializers import DestinoSerializer, PublicacionSerializer
from publicacion.models import Publicacion
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import Token
from rest_framework.pagination import PageNumberPagination


class PublicacionPagination(PageNumberPagination):
    page_size_query_param = 'page_size'  # Permitir que el cliente pase el tamaño de página con el parámetro 'page_size'
    max_page_size = 15

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
    
    paginator = PublicacionPagination()
    result_page = paginator.paginate_queryset(publicaciones, request)

    serializer = PublicacionSerializer(result_page, many=True)
    return Response(serializer.data)



def obtener_token(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key}, status=200)
        return JsonResponse({'error': 'Credenciales inválidas'}, status=400)

# Create your views here.

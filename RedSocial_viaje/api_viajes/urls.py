from django.urls import path
from . import views
from .views import filtrar_publicaciones
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('destinos/', views.listar_destinos, name='listar-destinos'),
    path('publicaciones/filtrar/', filtrar_publicaciones, name='filtrar-publicaciones'),
    path('api/token/', obtain_auth_token, name='api-token'),
]

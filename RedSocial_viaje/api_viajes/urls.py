from django.urls import path
from . import views
from .views import filtrar_publicaciones

urlpatterns = [
    path('destinos/', views.listar_destinos, name='listar-destinos'),
    path('publicaciones/filtrar/', filtrar_publicaciones, name='filtrar-publicaciones'),
]

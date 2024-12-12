from django.urls import path
from . import views

urlpatterns = [
    path('', views.destino_list, name='destino_list'),
    path('crear/', views.destino_create, name='destino_create'),
    path('<int:pk>/editar/', views.destino_edit, name='destino_edit'),
    path('<int:pk>/eliminar/', views.destino_delete, name='destino_delete'),
]

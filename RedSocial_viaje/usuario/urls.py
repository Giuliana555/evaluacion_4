from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuario_list, name='usuario_list'),  # Descomentar esta línea
    path('usuarios/', views.usuario_list, name='usuario_create'),
    path('<int:pk>/editar/', views.usuario_edit, name='usuario_edit'),
    path('<int:pk>/eliminar/', views.usuario_delete, name='usuario_delete'),
]
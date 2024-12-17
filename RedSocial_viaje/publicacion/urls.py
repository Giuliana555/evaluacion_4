from django.urls import path
from . import views

urlpatterns = [
    path('', views.publicacion_list, name='publicacion_list'),
    path('crear/', views.publicacion_create, name='publicacion_create'),
    path('buscar/', views.publicacion_search, name='publicacion_search'),
    path('<int:pk>/editar/', views.publicacion_edit, name='publicacion_edit'),
    path('<int:pk>/eliminar/', views.publicacion_delete, name='publicacion_delete'),
]

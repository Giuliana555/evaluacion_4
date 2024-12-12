from django.shortcuts import render, get_object_or_404, redirect
from .models import Publicacion
from usuario.models import Usuario
from destino.models import Destino

# Create your views here.


# Listar publicaciones
def publicacion_list(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'publicacion/publicacion_list.html', {'publicaciones': publicaciones})

# Crear publicación
def publicacion_create(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        destino_id = request.POST.get('destino_id')
        texto = request.POST.get('texto')

        usuario = get_object_or_404(Usuario, id=usuario_id)
        destino = get_object_or_404(Destino, id=destino_id)

        # Crear instancia de Publicacion y guardar en la base de datos
        Publicacion.objects.create(usuario=usuario, destino=destino, texto=texto)
        return redirect('publicacion_list')
    usuarios = Usuario.objects.all()
    destinos = Destino.objects.all()
    return render(request, 'publicacion/publicacion_form.html', {'usuarios': usuarios, 'destinos': destinos})

# Editar publicación
def publicacion_edit(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        publicacion.usuario_id = request.POST.get('usuario_id')
        publicacion.destino_id = request.POST.get('destino_id')
        publicacion.texto = request.POST.get('texto')
        publicacion.save()
        return redirect('publicacion_list')
    usuarios = Usuario.objects.all()
    destinos = Destino.objects.all()
    return render(request, 'publicacion/publicacion_form.html', {'publicacion': publicacion, 'usuarios': usuarios, 'destinos': destinos})

# Eliminar publicación
def publicacion_delete(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('publicacion_list')
    return render(request, 'publicacion/publicacion_confirm_delete.html', {'publicacion': publicacion})

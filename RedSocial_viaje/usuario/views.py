from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Usuario

# Create your views here.
def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario_list.html', {'usuarios': usuarios})

# Editar usuario
@login_required
def usuario_edit(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    # Verificar si el usuario actual puede editar este perfil
    if request.user != usuario and not request.user.is_superuser:
        return redirect('publicacion_list')  # Redirige si no es su perfil o superusuario

    if request.method == 'POST':
        usuario.nombre = request.POST.get('nombre')
        usuario.correo = request.POST.get('correo')
        usuario.ubicacion = request.POST.get('ubicacion')
        usuario.save()
        return redirect('usuario_list')  # Redirige a publicaciones

    return render(request, 'usuario_form.html', {'usuario': usuario})

# Eliminar usuario
def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuario_confirm_delete.html', {'usuario': usuario})


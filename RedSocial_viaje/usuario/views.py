from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario

# Create your views here.

# Crear usuario
def usuario_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        ubicacion = request.POST.get('ubicacion')
        
        # Crear instancia de Usuario y guardar en la base de datos
        Usuario.objects.create(nombre=nombre, correo=correo, ubicacion=ubicacion)
        return redirect('usuario_list')
    return render(request, 'usuario/usuario_form.html')

# Editar usuario
def usuario_edit(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.nombre = request.POST.get('nombre')
        usuario.correo = request.POST.get('correo')
        usuario.ubicacion = request.POST.get('ubicacion')
        usuario.save()
        return redirect('usuario_list')
    return render(request, 'usuario/usuario_form.html', {'usuario': usuario})

# Eliminar usuario
def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuario/usuario_confirm_delete.html', {'usuario': usuario})

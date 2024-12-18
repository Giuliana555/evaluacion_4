from django.shortcuts import render, get_object_or_404, redirect
from .models import Destino
from django.contrib.auth.decorators import login_required

# Listar destinos
@login_required
def destino_list(request):
    destinos = Destino.objects.all()
    return render(request, 'destino_list.html', {'destinos': destinos})

# Crear destino
@login_required
def destino_create(request):
    if request.method == 'POST':
        pais = request.POST.get('pais')
        ciudad = request.POST.get('ciudad')
        descripcion = request.POST.get('descripcion')

        # Crear instancia de Destino y guardar en la base de datos
        Destino.objects.create(pais=pais, ciudad=ciudad, descripcion=descripcion)
        return redirect('destino_list')
    return render(request, 'destino_form.html')

# Editar destino
@login_required
def destino_edit(request, pk):
    destino = get_object_or_404(Destino, pk=pk)
    if request.method == 'POST':
        destino.pais = request.POST.get('pais')
        destino.ciudad = request.POST.get('ciudad')
        destino.descripcion = request.POST.get('descripcion')
        destino.save()
        return redirect('destino_list')
    return render(request, 'destino_form.html', {'destino': destino})

# Eliminar destino
@login_required
def destino_delete(request, pk):
    destino = get_object_or_404(Destino, pk=pk)
    if request.method == 'POST':
        destino.delete()
        return redirect('destino_list')
    return render(request, 'destino_confirm_delete.html', {'destino': destino})

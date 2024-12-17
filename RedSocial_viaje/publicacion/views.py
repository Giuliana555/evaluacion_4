from django.shortcuts import render, get_object_or_404, redirect
from .models import Publicacion
from usuario.models import Usuario
from destino.models import Destino
import requests
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD

=======
>>>>>>> 49b9acdcbb373c37c908215009c43882f55a94c3

# Create your views here.


# Listar publicaciones
@login_required
def publicacion_list(request):
<<<<<<< HEAD
    """
    Muestra todas las publicaciones. 
    Los botones de editar/eliminar se gestionan desde los templates.
    """
=======

>>>>>>> 49b9acdcbb373c37c908215009c43882f55a94c3
    publicaciones = Publicacion.objects.all()  # Todos los usuarios ven todas las publicaciones
    return render(request, 'publicacion_list.html', {'publicaciones': publicaciones})


# Crear publicación
@login_required
def publicacion_create(request):
    if request.method == 'POST':
        texto = request.POST.get('texto')
        destino_id = request.POST.get('destino_id')
        nueva_ciudad = request.POST.get('nueva_ciudad')
        nuevo_pais = request.POST.get('nuevo_pais')

        # Verificar si el usuario ingresó un destino existente o uno nuevo
        if destino_id:
            destino = get_object_or_404(Destino, id=destino_id)
        elif nueva_ciudad and nuevo_pais:
            destino, created = Destino.objects.get_or_create(ciudad=nueva_ciudad, pais=nuevo_pais)
        else:
            return render(request, 'publicacion_form.html', {
                'error': 'Debe seleccionar un destino o ingresar uno nuevo.',
                'destinos': Destino.objects.all()
            })

        # Crear la publicación
        Publicacion.objects.create(
            usuario=request.user,
            destino=destino,
            texto=texto
        )
        return redirect('publicacion_list')

    # Enviar destinos existentes al formulario
    destinos = Destino.objects.all()
    return render(request, 'publicacion_form.html', {'destinos': destinos})


# Editar publicación
@login_required
def publicacion_edit(request, pk):
<<<<<<< HEAD
    """
    Permite editar una publicación.
    Restricción: Solo el autor o un superusuario pueden editar.
    """
=======

>>>>>>> 49b9acdcbb373c37c908215009c43882f55a94c3
    publicacion = get_object_or_404(Publicacion, pk=pk)

    if request.user != publicacion.usuario and not request.user.is_superuser:
        # Redirigir si no tiene permiso
        return redirect('publicacion_list')

    if request.method == 'POST':
        publicacion.destino_id = request.POST.get('destino_id')
        publicacion.texto = request.POST.get('texto')
        publicacion.save()
        return redirect('publicacion_list')

    destinos = Destino.objects.all()
    return render(request, 'publicacion_form.html', {'publicacion': publicacion, 'destinos': destinos})

# Eliminar publicación
@login_required
def publicacion_delete(request, pk):
<<<<<<< HEAD
    """
    Permite eliminar una publicación.
    Restricción: Solo el autor o un superusuario pueden eliminar.
    """
=======

>>>>>>> 49b9acdcbb373c37c908215009c43882f55a94c3
    publicacion = get_object_or_404(Publicacion, pk=pk)

    if request.user != publicacion.usuario and not request.user.is_superuser:
        # Redirigir si no tiene permiso
        return redirect('publicacion_list')

    if request.method == 'POST':
        publicacion.delete()
        return redirect('publicacion_list')

    return render(request, 'publicacion_confirm_delete.html', {'publicacion': publicacion})

@login_required
def publicacion_search(request):
    # URL de la API
    api_url = 'http://127.0.0.1:8000/api/publicaciones/filtrar/'  
    params = {}

    # Parámetros de búsqueda desde GET
    if 'usuario' in request.GET and request.GET['usuario']:
        params['usuario'] = request.GET['usuario']
    if 'destino' in request.GET and request.GET['destino']:
        params['destino'] = request.GET['destino']

    # Llamada a la API
    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            publicaciones = response.json()
        else:
            publicaciones = []  # Si la API falla
    except Exception as e:
        print(e)
        publicaciones = []  # Manejo de errores en la API

    # Obtener usuarios y destinos
    usuarios = Usuario.objects.all()
    destinos = Destino.objects.all()

    return render(
        request, 
        'publicacion_search.html', 
        {
            'publicaciones': publicaciones,
            'usuarios': usuarios,
            'destinos': destinos
        }
    )

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')  # Redirigir al login tras el registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
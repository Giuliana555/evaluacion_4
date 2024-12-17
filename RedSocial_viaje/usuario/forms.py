from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario  # Usar tu modelo de usuario personalizado
        fields = ['correo', 'password1', 'password2', 'nombre']  # Campos que aparecerán en el formulario

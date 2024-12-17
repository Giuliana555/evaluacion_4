from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
import uuid


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['correo', 'password1', 'password2', 'nombre']

    def save(self, commit=True):
        user = super().save(commit=False)
        if not user.username:  # Generar un username único si no se proporciona
            user.username = str(uuid.uuid4())[:30]  # Máximo 30 caracteres
        if commit:
            user.save()
        return user



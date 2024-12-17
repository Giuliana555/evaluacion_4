from rest_framework import serializers
from usuario.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    def validate_nombre(self, value):
        if not value.replace(' ', '').isalpha():
            raise serializers.ValidationError("El nombre debe contener solo letras y espacios.")
        return value

    def validate_correo(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Debe proporcionar un correo electrónico válido.")
        return value

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'correo', 'ubicacion']
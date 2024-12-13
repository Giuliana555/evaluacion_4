from rest_framework import serializers
from destino.models import Destino

class DestinoSerializer(serializers.ModelSerializer):
    def validate_pais(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("El nombre del país debe contener solo letras.")
        return value

    def validate_ciudad(self, value):
        if not value:
            raise serializers.ValidationError("La ciudad no puede estar vacía.")
        return value

    class Meta:
        model = Destino
        fields = ['id', 'pais', 'ciudad', 'descripcion']
from rest_framework import serializers
from .models import Parcela


class ParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcela
        fields = [
            'id', 'nombre', 'cultivo', 'superficie_ha', 'lat', 'lon', 'descripcion',
            'creado_en', 'actualizado_en'
        ]
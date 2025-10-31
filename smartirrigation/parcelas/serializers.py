from rest_framework import serializers
from .models import Parcela, Sensor, Lectura

class ParcelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcela
        fields = [
            'id', 'nombre', 'cultivo', 'superficie_ha', 'lat', 'lon', 'descripcion',
            'creado_en', 'actualizado_en'
        ]
        read_only_fields = ('id', 'creado_en', 'actualizado_en')

    def validate_superficie_ha(self, value):
        if value is None or value <= 0:
            raise serializers.ValidationError('Debe ser mayor que 0.')
        return value

    def validate_lat(self, value):
        if value is None or not (-90 <= value <= 90):
            raise serializers.ValidationError('Latitud fuera de rango (-90 a 90).')
        return value

    def validate_lon(self, value):
        if value is None or not (-180 <= value <= 180):
            raise serializers.ValidationError('Longitud fuera de rango (-180 a 180).')
        return value

class SensorSerializer(serializers.ModelSerializer):
    parcela_nombre = serializers.CharField(source="parcela.nombre", read_only=True)


    class Meta:
        model = Sensor
        fields = [
            "id", "parcela", "parcela_nombre", "codigo", "tipo", "unidad",
            "intervalo_seg", "estado", "ultima_lectura_valor", "ultima_lectura_ts",
            "creado_en", "actualizado_en"
        ]

class LecturaSerializer(serializers.ModelSerializer):
    sensor_codigo = serializers.CharField(source="sensor.codigo", read_only=True)


    class Meta:
        model = Lectura
        fields = ["id", "sensor", "sensor_codigo", "ts", "valor"]

    def validate_valor(self, v):
        # Ajusta si tu métrica necesita rango (ej. 0–100 para humedad %)
        if v is None:
            raise serializers.ValidationError('El valor es obligatorio.')
        return v
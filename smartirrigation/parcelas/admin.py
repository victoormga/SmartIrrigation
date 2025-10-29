from django.contrib import admin
from .models import Parcela, Sensor


@admin.register(Parcela)
class ParcelaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cultivo", "superficie_ha", "lat", "lon", "actualizado_en")
    search_fields = ("nombre", "cultivo")

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ("codigo", "tipo", "parcela", "estado", "ultima_lectura_valor", "ultima_lectura_ts")
    list_filter = ("tipo", "estado")
    search_fields = ("codigo", "parcela__nombre")
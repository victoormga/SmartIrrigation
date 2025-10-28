from django.contrib import admin
from .models import Parcela


@admin.register(Parcela)
class ParcelaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cultivo", "superficie_ha", "lat", "lon", "actualizado_en")
    search_fields = ("nombre", "cultivo")
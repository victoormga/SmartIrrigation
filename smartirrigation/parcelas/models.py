from django.db import models


class Parcela(models.Model):
    nombre = models.CharField(max_length=120)
    cultivo = models.CharField(max_length=120, blank=True)
    superficie_ha = models.DecimalField(max_digits=7, decimal_places=2, help_text="Hectáreas")
    lat = models.DecimalField(max_digits=9, decimal_places=6, help_text="Latitud WGS84")
    lon = models.DecimalField(max_digits=9, decimal_places=6, help_text="Longitud WGS84")
    descripcion = models.TextField(blank=True)


    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["nombre"]
        indexes = [
            models.Index(fields=["nombre"]),
        ]


    def __str__(self):
        return self.nombre
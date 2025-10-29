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
    

class Sensor(models.Model):
    class Tipo(models.TextChoices):
        HUMEDAD_SUELO = "humedad_suelo", "Humedad de suelo"
        TEMPERATURA = "temperatura", "Temperatura"
        CAUDAL = "caudal", "Caudal"
        PH = "ph", "pH"
        CONDUCTIVIDAD = "conductividad", "Conductividad"


    class Estado(models.TextChoices):
        ACTIVO = "activo", "Activo"
        INACTIVO = "inactivo", "Inactivo"
        MANTENIMIENTO = "mantenimiento", "Mantenimiento"


    parcela = models.ForeignKey(Parcela, on_delete=models.CASCADE, related_name="sensores")
    codigo = models.CharField(max_length=80, unique=True) # identificador del dispositivo
    tipo = models.CharField(max_length=32, choices=Tipo.choices)
    unidad = models.CharField(max_length=16, blank=True, help_text="Ej.: %, °C, L/min")
    intervalo_seg = models.PositiveIntegerField(default=900, help_text="Frecuencia esperada de muestreo")


    estado = models.CharField(max_length=16, choices=Estado.choices, default=Estado.ACTIVO)
    ultima_lectura_valor = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    ultima_lectura_ts = models.DateTimeField(null=True, blank=True)


    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["parcela__nombre", "codigo"]
        indexes = [
            models.Index(fields=["codigo"]),
            models.Index(fields=["tipo"]),
        ]


    def __str__(self):
        return f"{self.codigo} ({self.get_tipo_display()})"
    

class Lectura(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="lecturas")
    ts = models.DateTimeField() # timestamp de la muestra
    valor = models.DecimalField(max_digits=10, decimal_places=3)


    class Meta:
        ordering = ["-ts"]
        indexes = [
            models.Index(fields=["sensor", "ts"]),
        ]


    def __str__(self):
        return f"{self.sensor.codigo}@{self.ts}: {self.valor}"
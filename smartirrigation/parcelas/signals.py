from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lectura, Sensor

@receiver(post_save, sender=Lectura)
def actualizar_ultima_lectura(sender, instance, created, **kwargs):
    if created:
        sensor = instance.sensor
        # Solo si es más reciente
        if (sensor.ultima_lectura_ts is None) or (instance.ts >= sensor.ultima_lectura_ts):
            sensor.ultima_lectura_valor = instance.valor
            sensor.ultima_lectura_ts = instance.ts
            sensor.save(update_fields=['ultima_lectura_valor', 'ultima_lectura_ts'])

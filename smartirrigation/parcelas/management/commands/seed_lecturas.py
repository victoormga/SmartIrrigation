from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from parcelas.models import Sensor, Lectura
import random

class Command(BaseCommand):
    help = "Genera lecturas sintéticas para sensores existentes"

    def handle(self, *args, **kwargs):
        ahora = timezone.now()
        sensores = Sensor.objects.all()
        if not sensores.exists():
            self.stdout.write(self.style.WARNING("No hay sensores. Crea alguno primero."))
            return

        for s in sensores:
            for i in range(12):  # 12 muestras
                ts = ahora - timedelta(minutes=10*i)
                valor = round(random.uniform(15, 40), 2)
                Lectura.objects.get_or_create(sensor=s, ts=ts, defaults={'valor': valor})
        self.stdout.write(self.style.SUCCESS("Lecturas sintéticas generadas."))
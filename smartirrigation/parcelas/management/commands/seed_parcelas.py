from django.core.management.base import BaseCommand
from parcelas.models import Parcela


class Command(BaseCommand):
    help = "Crea parcelas de ejemplo"


    def handle(self, *args, **kwargs):
        ejemplos = [
            {"nombre": "Norte", "cultivo": "Olivo", "superficie_ha": 2.5, "lat": 37.389092, "lon": -5.984459},
            {"nombre": "Sur", "cultivo": "Vid", "superficie_ha": 1.8, "lat": 37.390100, "lon": -5.980000},
        ]
        for e in ejemplos:
            Parcela.objects.get_or_create(
                nombre=e["nombre"],
                defaults={
                    "cultivo": e["cultivo"],
                    "superficie_ha": e["superficie_ha"],
                    "lat": e["lat"],
                    "lon": e["lon"],
                }
            )
        self.stdout.write(self.style.SUCCESS("Parcelas de ejemplo creadas."))
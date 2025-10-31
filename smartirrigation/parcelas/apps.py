from django.apps import AppConfig


class ParcelasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parcelas'

    def ready(self):
        from . import signals
from django.apps import AppConfig


class PerdidosConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'apps.perdidos'

   def ready(self) -> None:
      import apps.suscripcion.signals
      return super().ready()
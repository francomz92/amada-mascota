from django.apps import AppConfig


class AdopcionConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'apps.adopcion'

   def ready(self) -> None:
      import apps.suscripcion.signals
      return super().ready()
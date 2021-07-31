from django.apps import AppConfig


class EncontradosConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'apps.encontrados'

   def ready(self) -> None:
      import apps.suscripcion.signals
      return super().ready()
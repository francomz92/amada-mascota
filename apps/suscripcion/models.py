from apps.usuario.models import User
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
LISTA_SUSCRIPCIONES = (
    ('Encontrados', 'Encontrados'),
    ('Perdidos', 'Perdidos'),
    ('Adopcion', 'Adopción'),
)


class Suscripcion(models.Model):
   id_usuario = models.ForeignKey(verbose_name='Usuario', to=User, on_delete=models.CASCADE)
   suscripcion = models.CharField(
       max_length=15,
       choices=LISTA_SUSCRIPCIONES,
   )
   active = models.BooleanField(default=True)

   def __suscripcion_field_validator(self):
      suscriptions_list = list(element[0] for element in LISTA_SUSCRIPCIONES)
      if self.suscripcion not in suscriptions_list:
         raise ValidationError('¡La opción ingresada no se encuentra en la lista!')

   def clean(self) -> None:
      self.__suscripcion_field_validator()
      return super().clean()

   class Meta:
      verbose_name = 'Suscripción'
      verbose_name_plural = 'Suscripciones'
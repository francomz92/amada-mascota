from django.core.exceptions import ValidationError
from django.utils.timezone import now
from apps.models import Publicacion
from django.db import models

from django.core.validators import MaxValueValidator
# Create your models here.

EN_TRANSITO = (
    ('Si', 'Si'),
    ('No', 'No'),
)


class Encontro(Publicacion):
   fecha_encontrado = models.DateField(
       help_text='¿Cuándo lo encontro?',
       validators=[MaxValueValidator(now().date(), '¡La fecha no puede ser mayor a hoy!')],
   )
   cuida = models.CharField(
       verbose_name='En transito',
       max_length=2,
       choices=EN_TRANSITO,
       help_text='Si está cuidando al animalito indique Si, en caso contrario indique No')

   def in_transito(self):
      return True if self.cuida == 'Si' else False

   def __cuida_field_validator(self):
      en_trancito_list = list(element[0] for element in EN_TRANSITO)
      if self.cuida not in en_trancito_list:
         raise ValidationError('¡La opción ingresada no se encuentra en la lista!')

   def clean(self) -> None:
      self.__cuida_field_validator()
      return super().clean()

   def save(self, *arrgs, **kwargs) -> None:
      self.full_clean()
      return super().save(*arrgs, **kwargs)

   def __str__(self):
      return f'{self.id_mascota.especie} {self.id_ubicacion.localidad}, {self.id_ubicacion.barrio} - {self.fecha_encontrado}'

   class Meta:
      verbose_name = 'Encontrado'
      verbose_name_plural = 'Encontrados'

from django.core.validators import MaxLengthValidator
from apps.models import Publicacion
from django.db import models

# Create your models here.


class Adopcion(Publicacion):
   condicion = models.TextField(
       verbose_name='condiciones',
       max_length=800,
       validators=[MaxLengthValidator(800, '¡Máximo permitido 800 caracteres!')],
   )

   def save(self, *arrgs, **kwargs) -> None:
      self.full_clean()
      return super().save(*arrgs, **kwargs)

   def __str__(self):
      return f'{self.id_mascota.especie} - {self.id_ubicacion.localidad}, {self.id_ubicacion.barrio} - {self.fecha_publicacion}'

   class Meta:
      verbose_name = 'Adopcion'
      verbose_name_plural = 'Adopciones'

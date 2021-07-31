from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.utils.timezone import now
from apps.models import Publicacion
from django.db import models

# Create your models here.


class Perdido(Publicacion):
   edad = models.IntegerField(
       validators=[
           MinValueValidator(0, '¡No se permiten edades negativas!'),
           MaxValueValidator(25, '¡Máximo permitido 25 años!'),
           ],
       )
   fecha_perdido = models.DateField(
       help_text='¿Cuándo se perdió?',
       validators=[MaxValueValidator(now().date(), '¡La fecha no puede ser mayor a hoy!')],
       )
   gratificacion = models.CharField(
       max_length=150,
       help_text='Si ofrece gratificación detalle aqui',
       null=True,
       blank=True,
       )

   def __str__(self):
      return f'{self.id_mascota.especie} {self.id_ubicacion.localidad}, {self.id_ubicacion.barrio} - {self.fecha_perdido}'

   def save(self, *args, **kwargs) -> None:
      self.full_clean()
      return super().save(*args, **kwargs)

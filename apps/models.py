from django.core.exceptions import ValidationError
from django.utils.timezone import now, timedelta
from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator
from apps.usuario.models import User

# <---------- Mascota Model ----------> #

LISTA_ESPECIES = (
    ('Conejo', 'Conejo'),
    ('Gato', 'Gato'),
    ('Loro', 'Loro'),
    ('Perro', 'Perro'),
    ('Tortuga', 'Tortuga'),
)
LISTA_TAMANOS = (
    ('Grande', 'Grande'),
    ('Mediano', 'Mediano'),
    ('Chico', 'Chico'),
)
LISTA_SEXOS = (
    ('Macho', 'Macho'),
    ('Hembra', 'Hembra'),
    ('Desconocido', 'Desconocido'),
)


class Mascota(models.Model):
   nombre = models.CharField(
       max_length=30,
       help_text="Indica su nombre si lo conoces",
       null=True,
       blank=True,
       validators=[MaxLengthValidator(30, '¡Máximo permitido 30 caracteres!')],
   )
   especie = models.CharField(
       max_length=7,
       choices=LISTA_ESPECIES,
       null=False,
       validators=[MaxLengthValidator(7, '¡Máximo permitido 7 caracteres!')],
   )
   raza = models.CharField(
       max_length=40,
       null=True,
       blank=True,
       validators=[MaxLengthValidator(40, '¡Máximo permitido 40 caracteres!')],
   )
   tamano = models.CharField(
       max_length=7,
       choices=LISTA_TAMANOS,
       null=False,
       validators=[MaxLengthValidator(7, '¡Máximo permitido 7 caracteres!')],
   )

   sexo = models.CharField(
       max_length=11,
       choices=LISTA_SEXOS,
       null=False,
       validators=[MaxLengthValidator(11, '¡Máximo permitido 11 caracteres!')],
   )
   fotos = models.ImageField(upload_to='mascota', null=True, blank=True)
   otro_dato = models.TextField(
       verbose_name='Otra información',
       max_length=255,
       null=True,
       blank=True,
       validators=[MaxLengthValidator(255, '¡Máximo permitido 255 caracteres!')],
   )

   def __set_nombre(self):
      if not self.nombre:
         self.nombre = 'Desconocido'

   def __especie_field_validation(self):
      species_list = list(element[0] for element in LISTA_ESPECIES)
      if self.especie not in species_list:
         raise ValidationError('¡La opción ingresada no se encuentra en la lista!')

   def __tamano_field_validator(self):
      size_list = list(element[0] for element in LISTA_TAMANOS)
      if self.tamano not in size_list:
         raise ValidationError('¡La opción ingresada no se encuentra en la lista!')

   def __sexo_field_validator(self):
      sex_list = list(element[0] for element in LISTA_SEXOS)
      if self.sexo not in sex_list:
         raise ValidationError('¡La opción ingresada no se encuentra en la lista!')

   def clean(self) -> None:
      self.__set_nombre()
      self.__especie_field_validation()
      self.__tamano_field_validator()
      self.__sexo_field_validator()
      return super().clean()

   def save(self, *args, **kwargs):
      self.full_clean()
      return super().save(*args, **kwargs)

   def __str__(self):
      return f'{self.especie}: {self.nombre}'


# <---------- Ubicación Model ----------> #

LISTA_LOCALIDADES = (
    ('Avia Terai', 'Avia Terai'),
    ('Campo Largo', 'Campo Largo'),
    ('Charata', 'Charata'),
    ('Colonia Benítez', 'Colonia Benítez'),
    ('Colonia Elisa', 'Colonia Elisa'),
    ('Colonias Unida', 'Colonias Unidas'),
    ('Comandancia Frías', 'Comandancia Frías'),
    ('Concepción del Bermejo', 'Concepción del Bermejo'),
    ('Coronel Du Graty', 'Coronel Du Graty'),
    ('Corzuela', 'Corzuela'),
    ('El Paranacito', 'El Paranacito'),
    ('El Sauzalito', 'El Sauzalito'),
    ('Fortín Belgrano', 'Fortín Belgrano'),
    ('Gancedo', 'Gancedo'),
    ('Gral. José de San Martín', 'Gral. José de San Martín'),
    ('Gral. Pinedo', 'Gral. Pinedo'),
    ('Hermoso Campo', 'Hermoso Campo'),
    ('Isla Soto', 'Isla Soto'),
    ('Juan José Castelli', 'Juan José Castelli'),
    ('La Clotilde', 'La Clotilde'),
    ('La Escondida', 'La Escondida'),
    ('La Leonesa', 'La Leonesa'),
    ('La Tigra', 'La Tigra'),
    ('La Verde', 'La Verde'),
    ('Las Breñas', 'Las Breñas'),
    ('Las Garcitas', 'Las Garcitas'),
    ('Las Hacheras', 'Las Hacheras'),
    ('Las Palmas', 'Las Palmas'),
    ('Los Frentones', 'Los Frentones'),
    ('Machagai', 'Machagai'),
    ('Makallé', 'Makallé'),
    ('Margarita Belén', 'Margarita Belén'),
    ('Miraflores', 'Miraflores'),
    ('Misión Nueva Pompeya', 'Misión Nueva Pompeya'),
    ('Napenay', 'Napenay'),
    ('Pampa del Indio', 'Pampa del Indio'),
    ('Pampa del Infierno', 'Pampa del Infierno'),
    ('Presidencia de la Plaza', 'Presidencia de la Plaza'),
    ('Presidencia Roca', 'Presidencia Roca'),
    ('Presidencia Roque Sáenz Peña', 'Presidencia Roque Sáenz Peña'),
    ('Puerto Bermejo', 'Puerto Bermejo'),
    ('Puerto Las Palmas', 'Puerto Las Palmas'),
    ('Puerto Tirol', 'Puerto Tirol'),
    ('Quitilipi', 'Quitilipi'),
    ('San Bernardo', 'San Bernardo'),
    ('Paraje San Fernando', 'Paraje San Fernando'),
    ('Santa Sylvina', 'Santa Sylvina'),
    ('Taco Pozo', 'Taco Pozo'),
    ('Tres Isletas', 'Tres Isletas'),
    ('Villa Ángela', 'Villa Ángela'),
    ('Villa Berthet', 'Villa Berthet'),
    ('Villa Río Bermejito', 'Villa Río Bermejito'),
)


class Ubicacion(models.Model):
   localidad = models.CharField(
       max_length=30,
       choices=LISTA_LOCALIDADES,
       null=False,
       validators=[MaxLengthValidator(30, '¡Máximo permitido 30 caracteres!')],
   )
   barrio = models.CharField(
       max_length=50,
       validators=[MaxLengthValidator(50, '¡Máximo permitido 50 caracteres!')],
   )
   calle = models.CharField(
       max_length=50,
       null=True,
       blank=True,
       validators=[MaxLengthValidator(50, '¡Máximo permitido 50 caracteres!')],
   )
   numero = models.CharField(
       max_length=5,
       default="S/N",
       null=True,
       blank=True,
       validators=[MaxLengthValidator(5, '¡Máximo permitido 5 caracteres!')],
   )
   entre_calles = models.CharField(
       max_length=50,
       null=True,
       blank=True,
       validators=[MaxLengthValidator(50, '¡Máximo permitido 50 caracteres!')],
   )
   referencia = models.TextField(
       verbose_name='Alguna referencia',
       max_length=200,
       null=True,
       blank=True,
       validators=[MaxLengthValidator(200, '¡Máximo permitido 200 caracteres!')],
   )

   def __localidad_field_validator(self):
      localities_list = list(element[0] for element in LISTA_LOCALIDADES)
      if self.localidad not in localities_list:
         raise ValidationError('¡La opción ingresada no se encuentra en la lista!')

   def clean(self) -> None:
      self.__localidad_field_validator()
      return super().clean()

   def save(self, *args, **kwargs):
      self.full_clean()
      return super().save(*args, **kwargs)

   def __str__(self):
      return f'{self.localidad} - {self.barrio}'

   class Meta:
      verbose_name = 'Ubicación'
      verbose_name_plural = 'Ubicaciones'


# <---------- Publicación Model ----------> #


class Publicacion(models.Model):
   id_usuario = models.ForeignKey(
       to=User,
       on_delete=models.CASCADE,
   )
   id_mascota = models.ForeignKey(
       to=Mascota,
       on_delete=models.CASCADE,
   )
   id_ubicacion = models.ForeignKey(
       to=Ubicacion,
       on_delete=models.DO_NOTHING,
   )
   fecha_publicacion = models.DateField(auto_now_add=True)
   valido_hasta = models.DateField(
       default=(now() + timedelta(days=7)).date(),
       null=True,
       editable=True,
   )
   fecha_entrega = models.DateField(
       default=None,
       null=True,
       blank=True,
       editable=True,
       validators=[MaxValueValidator(now().date(), '¡La fecha no puede ser mayor a hoy!')],
   )

   def renovar_fecha_vencimiento(self):
      self.valido_hasta = (now() + timedelta(days=7)).date()
      self.save()

   def set_fecha_entrega(self):
      self.fecha_entrega = now().date()
      self.valido_hasta = None
      self.save()

   def is_active(self):
      return True if self.fecha_entrega is None else False

   def __str__(self):
      fecha = f'{self.fecha_publicacion.day}/{self.fecha_publicacion.month}'
      return f'{self.id_mascota.especie} - {self.id_ubicacion.localidad}, {self.id_ubicacion.barrio} - {fecha}'

   class Meta:
      verbose_name = 'Publicación'
      verbose_name_plural = 'Publicaciones'

from django.core.exceptions import ValidationError
from apps.encontrados.models import Encontro
from datetime import timedelta
from django.utils.timezone import now
from apps.usuario.models import User
from apps.models import Mascota, Ubicacion
from django.test import TestCase


class EncontradoModeTest(TestCase):

   # -----> Tests settings <----- #

   def setUp(self) -> None:
      self.mascota = Mascota.objects.create(nombre='Pepe', especie='Perro', tamano='Grande', sexo='Macho')
      self.ubicacion = Ubicacion.objects.create(localidad='Avia Terai', barrio='Libertad')
      self.usuario = User.objects.create(username='franco1992',
                                         email='franco1992@gmail.com',
                                         first_name='Franco',
                                         last_name='Muñoz',
                                         phone_number='12345678',
                                         password='12345678')
      return super().setUp()

   def tearDown(self) -> None:
      try:
         self.encontrado.delete()
      except:
         pass
      return super().tearDown()

   # -----> Fecha_encontrado validation errors <----- #

   def test_model_max_fecha_encontrado_exceeded(self):
      '''
         Al intentar crear un registro en Encontrado con una fecha de encontrado superiror a la actual se produce un ValidationError y el registro no se crea.
      '''
      fecha = (now() + timedelta(days=5)).date()
      # When
      error = None
      try:
         self.encontrado = Encontro.objects.create(id=18,
                                                   id_usuario=self.usuario,
                                                   id_mascota=self.mascota,
                                                   id_ubicacion=self.ubicacion,
                                                   fecha_encontrado=fecha,
                                                   cuida='Si')
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Encontro.objects.filter(id=18).first())

   # -----> Cuida validation errors <----- #

   def test_model_cuida_maximum_length_exceeded(self):
      '''
         Al intentar crear un registro en Encontrado con el campo cuida excediendo los 2 caracteres de longitud se produce un ValidationError y el registro no se crea.
      '''
      cuida = 'Si lo cuida'
      # When
      error = None
      try:
         self.encontrado = Encontro.objects.create(id=18,
                                                   id_usuario=self.usuario,
                                                   id_mascota=self.mascota,
                                                   id_ubicacion=self.ubicacion,
                                                   fecha_encontrado=now().date(),
                                                   cuida=cuida)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Encontro.objects.filter(id=18).first())
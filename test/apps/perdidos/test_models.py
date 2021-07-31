from django.utils.timezone import now, datetime
from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.models import Mascota, Ubicacion
from apps.usuario.models import User
from apps.perdidos.models import Perdido


class PerdidoModelTest(TestCase):

   # -----> Tests settings <----- #

   def setUp(self) -> None:
      self.mascota = Mascota.objects.create(nombre='Tobi',
                                            especie='Perro',
                                            raza='Pitbull',
                                            sexo='Macho',
                                            tamano='Grande')
      self.ubicacion = Ubicacion.objects.create(localidad='Juan José Castelli', barrio='Libertad')
      self.usuario = User.objects.create(username='franco1992',
                                         email='franco1992@gmail.com',
                                         first_name='Franco',
                                         last_name='Muñoz',
                                         phone_number='12345678',
                                         password='12345678')
      return super().setUp()

   def tearDown(self) -> None:
      try:
         self.object.delete()
      except:
         pass
      return super().tearDown()

# -----> Edad validation errors <----- #

   def test_edad_negativa(self):
      '''
         Al intentar crear un objeto Perdido con edad negativa "edad = -5" el objeto no se crea y devuelve un ValidationError.
      '''
      edad = -5
      # when
      error = None
      try:
         self.object = Perdido.objects.create(id=18,
                                              id_mascota=self.mascota,
                                              id_ubicacion=self.ubicacion,
                                              id_usuario=self.usuario,
                                              edad=edad,
                                              fecha_perdido=now().date(),
                                              gratificacion='$1000')
      except Exception as err:
         error = err
      # Then
      finally:
         self.assertEqual(type(error), ValidationError)
         self.assertIsNone(Perdido.objects.filter(id=18).first())
#

   def test_edad_mayor_a_25(self):
      '''
         Al intentar crear un objeto Perdido con edad mayor a 25 años "edad = 25" el objeto no se crea y devuelve un ValidationError.
      '''
      edad = 26
      # when
      error = None
      try:
         self.object = Perdido.objects.create(id=18,
                                              id_mascota=self.mascota,
                                              id_ubicacion=self.ubicacion,
                                              id_usuario=self.usuario,
                                              edad=edad,
                                              fecha_perdido=now().date(),
                                              gratificacion='$1000')
      except Exception as err:
         error = err
      # Then
      finally:
         self.assertEqual(type(error), ValidationError)
         self.assertIsNone(Perdido.objects.filter(id=18).first())

# -----> Fecha_perdido validation errors <----- #

   def test_fecha_perdido_superior_a_hoy(self):
      '''
         Al intentar crear un objeto Perdido con fecha futura "fecha = 20/12/2021" el objeto no se crea y devuelve un ValidationError.
      '''
      fecha = datetime(day=20, month=12, year=2022).date()
      # When
      error = None
      try:
         self.object = Perdido.objects.create(id=18,
                                              id_mascota=self.mascota,
                                              id_ubicacion=self.ubicacion,
                                              id_usuario=self.usuario,
                                              edad=5,
                                              fecha_perdido=fecha,
                                              gratificacion='$1000')
      except Exception as err:
         error = err
      # Then
      finally:
         self.assertEqual(type(error), ValidationError)
         self.assertIsNone(Perdido.objects.filter(id=18).first())


# -----> Gratificacion validation errors <----- #

   def test_gratificacion_max_150_caracteres(self):
      '''
         Al intentar crear un objeto Perdido con el campo gratificacion con un tamaño superior a 150 caracteres "gratificacion = 151" el objeto no se crea y devuelve un ValidationError.
      '''
      gratificacion = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis pa'
      # when
      error = None
      try:
         self.object = Perdido.objects.create(id=18,
                                              id_mascota=self.mascota,
                                              id_ubicacion=self.ubicacion,
                                              id_usuario=self.usuario,
                                              edad=5,
                                              fecha_perdido=now().date(),
                                              gratificacion=gratificacion)
      except Exception as err:
         error = err
      # then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Perdido.objects.filter(id=18).first())

from django.core.exceptions import ValidationError
from apps.adopcion.models import Adopcion
from apps.usuario.models import User
from apps.models import Mascota, Ubicacion
from django.test import TestCase


class AdopcionModeelTest(TestCase):

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
         self.adopcion.delete()
      except:
         pass
      return super().tearDown()

   # -----> Condicion validation errors <----- #

   def test_model_maximum_adopcion_length_exceeded(self):
      '''
         Al intentar crear un registro en Adopcion con el campo condicion excediendo los 800 caracteres de longitud se produce un ValidationError y el registro no se crea.
      '''

      condicion = \
         'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies.'
      # When
      error = None
      try:
         self.adopcion = Adopcion.objects.create(id=18,
                                                 id_usuario=self.usuario,
                                                 id_mascota=self.mascota,
                                                 id_ubicacion=self.ubicacion,
                                                 condicion=condicion)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Adopcion.objects.filter(id=18).first())
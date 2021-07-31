from apps.adopcion.forms import AdopcionForms
from django.test import TestCase


class AdopcionFormTest(TestCase):

   # -----> Tests settings <----- #

   def setUp(self) -> None:
      self.data = {'condicion': ''}
      return super().setUp()

   # -----> Condicion Error Messages <----- #

   def test_form_maximum_length_condicion(self):
      '''
         Al ingresar un texto con mas de 800 caracteres "condicion = Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies." devuelve un error con la leyenda "¡Máximo permitido 800 caracteres!" siendo el formulario ivalido (False).
      '''
      self.data['condicion'] = \
         'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies.'
      # When
      form = AdopcionForms(data=self.data)
      # Then
      self.assertIsNotNone(form.data)
      self.assertEqual(form.errors['condicion'], ['¡Máximo permitido 800 caracteres!'])
      self.assertFalse(form.is_valid())
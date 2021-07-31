from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils.timezone import now, timedelta
from apps.perdidos.forms import PerdidoForm


class PerdidoFormTest(TestCase):

   # -----> Tests settings <----- #

   def setUp(self) -> None:
      self.data = {'fecha_perdido': '2020-12-20', 'edad': 10, 'gratificacion': '$1000'}
      return super().setUp()

   # -----> Edad errors messages <----- #

   def test_form_negative_edad_error_message(self):
      '''
         Al ingresar una edad negativa "edad = -5" devuelve un error con la leyenda "¡No se permiten edades negativas!" siendo el formulario invalido (False).
      '''
      self.data['edad'] = -5
      # when
      form = PerdidoForm(data=self.data)
      # Then
      self.assertEqual(form.errors['edad'], ['¡No se permiten edades negativas!'])
      self.assertFalse(form.is_valid())


#

   def test_form_maximun_edad_exceeded(self):
      '''
         Al ingresar una edad superior a 25 años "edad = 26" devuelve un error con la leyenda "¡Máximo permitido 25 años!" siendo el formulario invalido (False).
      '''
      self.data['edad'] = 26
      # when
      form = PerdidoForm(data=self.data)
      # Then
      self.assertEqual(form.errors['edad'], ['¡Máximo permitido 25 años!'])
      self.assertFalse(form.is_valid())

   # -----> Fecha_perdido errors messages <----- #

   def test_form_maximum_fecha_perdido_exceeded(self):
      f'''
         Al ingresar una fecha superior a la actual "fecha_perdido = {(now() + timedelta(days=5)).date()}" devuelve un error con la leyenda "¡Máximo permitido 25 años!" siendo el formulario invalido (False).
      '''
      self.data['fecha_perdido'] = (now() + timedelta(days=5)).date()
      # When
      form = PerdidoForm(data=self.data)
      # Then
      self.assertEqual(form.errors['fecha_perdido'], ['¡La fecha no puede ser mayor a hoy!'])
      self.assertFalse(form.is_valid())

   # -----> Gratificacion errors messages <----- #

   def test_form_gratificacion_maximum_length_exceeded(self):
      '''
         Al ingresar un texto de mas de 150 caracteres "gratificacion = Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis pi" devuelve un error con la leyenda "¡Máximo permitido 25 años!" siendo el formulario invalido (False).
      '''
      self.data['gratificacion'] = \
             'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis pi'
      # When
      form = PerdidoForm(data=self.data)
      # Then
      self.assertEqual(form.errors['gratificacion'], ['¡Máximo permitido 150 caracteres!'])
      self.assertFalse(form.is_valid())
from datetime import timedelta
from django.utils.timezone import now
from django.test import TestCase
from apps.encontrados.forms import EncontradoForms


class EncontradoFormTest(TestCase):

   # -----> Tests settings <----- #

   def setUp(self) -> None:
      self.data = {'fecha_encontrado': now().date(), 'cuida': 'Si'}
      return super().setUp()

   # -----> Fecha_encontrado error message <----- #

   def test_form_maximum_fecha_encontrado_exceeded(self):
      f'''
         Al ingresar una fecha superior a la actual "fecha_perdido = {(now() + timedelta(days=5)).date()}" devuelve un error con la leyenda "¡La fecha no puede ser mayor a hoy!" siendo el formulario invalido (False).
      '''
      self.data['fecha_encontrado'] = (now() + timedelta(days=5)).date()
      # When
      form = EncontradoForms(data=self.data)
      # Then
      self.assertIsNotNone(form.data)
      self.assertEqual(form.errors['fecha_encontrado'], ['¡La fecha no puede ser mayor a hoy!'])
      self.assertFalse(form.is_valid())

   # -----> Cuida error message <----- #

   def test_form_cuida_maximum_length_exceeded(self):
      '''
         Al ingresar un valor que supere los 2 caracteres de longitud "cuida = Si lo cuido" devuelve un error con la leyenda "Seleccione una opción válida. Si lo cuido no es una de las opciones disponibles."
      '''
      self.data['cuida'] = 'Si lo cuido'
      # When
      form = EncontradoForms(data=self.data)
      # Then
      self.assertIsNotNone(form.data)
      self.assertEqual(form.errors['cuida'],
                       ['Seleccione una opción válida. Si lo cuido no es una de las opciones disponibles.'])
      self.assertFalse(form.is_valid())
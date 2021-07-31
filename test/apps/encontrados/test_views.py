from django.test import TestCase
from apps.usuario.models import User


class EncontradoViewTest(TestCase):

   # -----> Tests settings <----- #

   def setUp(self) -> None:
      self.user = User.objects.create(username='franco1992',
                                      email='franco1992@gmail.com',
                                      first_name='Franco',
                                      last_name='Muñoz',
                                      phone_number='12345678',
                                      password='12345678')
      return super().setUp()

   def tearDown(self) -> None:
      self.user.delete()
      return super().tearDown()

   # -----> PublicEncontradosView <----- #

   def test_public_encontrados_view_context_data(self):
      '''
         Al visitar el path /encontrados/ se envian las data "form", "publicaciones", "msj", "title" y "header" y ademas "msj" contiene el texto "Estas mascotas se encuentran sin dueño.", "title" contiene el texto "Encontrados" y "header" contiene el texto "Consulta Encontrados".
      '''
      # When
      response = self.client.get('/encontrados/')
      # Then
      self.assertIn('form', response.context)
      self.assertIn('publicaciones', response.context)
      self.assertIn('msj', response.context)
      self.assertIn('title', response.context)
      self.assertIn('header', response.context)
      self.assertIsNotNone(response.context['msj'])
      self.assertIsNotNone(response.context['title'])
      self.assertIsNotNone(response.context['header'])
      self.assertEqual(response.context['msj'], 'Estas mascotas se encuentran sin dueño.')
      self.assertEqual(response.context['title'], 'Encontrados')
      self.assertEqual(response.context['header'], 'Consulta Encontrados')

   # -----> PrivateEncontradosView <----- #

   def test_private_encontrados_view_context_data(self):
      '''
         Al visitar el path /encontrados/mis-publicaciones/ se envian las data "publicaciones", "msj", "title" y "header" y ademas "msj" contiene el texto "Estas mascotas se encuentran sin dueño.", "title" contiene el texto "Mis publicaciones" y "header" contiene el texto "Encontrados".
      '''
      # When
      self.client.force_login(self.user)
      response = self.client.get('/encontrados/mis-publicaciones/')
      # Then
      self.assertIn('publicaciones', response.context)
      self.assertIn('msj', response.context)
      self.assertIn('title', response.context)
      self.assertIn('header', response.context)
      self.assertIsNotNone(response.context['msj'])
      self.assertIsNotNone(response.context['title'])
      self.assertIsNotNone(response.context['header'])
      self.assertEqual(response.context['msj'], 'Estas mascotas se encuentran sin dueño.')
      self.assertEqual(response.context['title'], 'Mis Publicaciones')
      self.assertEqual(response.context['header'], 'Encontrados')

   # -----> PrivateCreateEncontradosView <----- #

   def test_private_creaete_encontrados_view_context_data(self):
      '''
         Al visitar el path /encontrados/publicar/ se envian las data, "msj", "title", "header", "form_class", "form_mascota", "form_ubicacion", y ademas "msj" contiene el texto "Publica una mascota encontrada.", "title" contiene el texto "Nueva Publicación" y "header" contiene el texto "Nueva Publicación".
      '''
      # When
      self.client.force_login(self.user)
      response = self.client.get('/encontrados/publicar/')
      # Then
      self.assertIn('title', response.context)
      self.assertIn('header', response.context)
      self.assertIn('msj', response.context)
      self.assertIn('form_class', response.context)
      self.assertIn('form_mascota', response.context)
      self.assertIn('form_ubicacion', response.context)
      self.assertIsNotNone(response.context['title'])
      self.assertIsNotNone(response.context['header'])
      self.assertIsNotNone(response.context['msj'])
      self.assertEqual(response.context['msj'], 'Publica una mascota encontrada.')
      self.assertEqual(response.context['title'], 'Nueva Publicación')
      self.assertEqual(response.context['header'], 'Nueva Publicación')

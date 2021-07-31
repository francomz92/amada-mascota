from apps.usuario.models import User
from django.test import TestCase


class PerdidoViewTest(TestCase):

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

   # -----> PublicPerdidosView <----- #

   def test_public_perdidos_view_context_data(self):
      '''
         Al visitar el path /perdidos/ se envian las data "form", "publicaciones", "msj", "title" y "header" y ademas "msj" contiene el texto "Estas mascotas necesitan reencontrarse con sus dueños.", "title" contiene el texto "Perdidos" y "header" contiene el texto "Consulta Perdidos".
      '''
      # When
      response = self.client.get('/perdidos/')
      # Then
      self.assertIn('form', response.context)
      self.assertIn('publicaciones', response.context)
      self.assertIn('msj', response.context)
      self.assertIn('title', response.context)
      self.assertIn('header', response.context)
      self.assertIsNotNone(response.context['msj'])
      self.assertIsNotNone(response.context['title'])
      self.assertIsNotNone(response.context['header'])
      self.assertEqual(response.context['msj'], 'Estas mascotas necesitan reencontrarse con sus dueños.')
      self.assertEqual(response.context['title'], 'Perdidos')
      self.assertEqual(response.context['header'], 'Consulta Perdidos')

   # -----> PrivatePerdidosView <----- #

   def test_private_perdidos_view_context_data(self):
      '''
         Al visitar el path /perdidos/mis-publicaciones/ se envian las data "publicaciones", "msj", "title" y "header" y ademas "msj" contiene el texto "Estas mascotas necesitan reencontrarse con sus dueños.", "title" contiene el texto "Mis publicaciones" y "header" contiene el texto "Perdidos".
      '''
      # When
      self.client.force_login(self.user)
      response = self.client.get('/perdidos/mis-publicaciones/')
      # Then
      self.assertIn('publicaciones', response.context)
      self.assertIn('msj', response.context)
      self.assertIn('title', response.context)
      self.assertIn('header', response.context)
      self.assertIsNotNone(response.context['msj'])
      self.assertIsNotNone(response.context['title'])
      self.assertIsNotNone(response.context['header'])
      self.assertEqual(response.context['msj'], 'Estas mascotas necesitan reencontrarse con sus dueños.')
      self.assertEqual(response.context['title'], 'Mis publicaciones')
      self.assertEqual(response.context['header'], 'Perdidos')

   # -----> PrivateCreatePerdidosView <----- #

   def test_private_creaete_perdidos_view_context_data(self):
      '''
         Al visitar el path /perdidos/publicar/ se envian las data, "msj", "title", "header", "form_class", "form_mascota", "form_ubicacion", y ademas "msj" contiene el texto "Publica una mascota perdida.", "title" contiene el texto "Nueva Publicación" y "header" contiene el texto "Nueva Publicación".
      '''
      # When
      self.client.force_login(self.user)
      response = self.client.get('/perdidos/publicar/')
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
      self.assertEqual(response.context['msj'], 'Publica una mascota perdida.')
      self.assertEqual(response.context['title'], 'Nueva Publicación')
      self.assertEqual(response.context['header'], 'Nueva Publicación')

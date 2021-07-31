from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.usuario.models import User


class UserModelTest(TestCase):

   # -----> Tests settings <----- #

   def setUp(self) -> None:
      self.username = 'pepe92'
      self.email = 'pepe92@gmail.com'
      self.first_name = 'pepe'
      self.last_name = 'lopez'
      self.phone_number = '1234'
      self.password = '12345678'
      return super().setUp()

   # -----> Username field test <----- #

   def test_username_field_maximum_length_exceeded(self) -> None:
      '''
         Al intentar registrar un usuario con un username que supere los 15 caracteres "username = Loremipsumdolo123" devuelve un ValidationError y no se crea el usuario.
      '''
      self.username = 'Loremipsumdolo123'
      # When
      error = None
      try:
         User.objects.create(id=18,
                             username=self.username,
                             email=self.email,
                             first_name=self.first_name,
                             last_name=self.last_name,
                             password=self.password)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(User.objects.filter(id=18).first())

#

   def test_username_field_white_space(self) -> None:
      '''
         Al intentar registrar un usuario con un username que contenga espacios en blanco "username =
         Lorem psumdo" devuelve un ValidationError y no se crea el usuario.
      '''
      self.username = 'Lorem psumdo'
      # When
      error = None
      try:
         User.objects.create(id=18,
                             username=self.username,
                             email=self.email,
                             first_name=self.first_name,
                             last_name=self.last_name,
                             password=self.password)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(User.objects.filter(id=18).first())

#

   def test_username_field_unique(self) -> None:
      '''
         Al intentar registrar un usuario con un username ya existente "username = pepito" devuelve un ValidationError y no se crea el usuario.
      '''
      username = 'pepito'
      # When
      error = None
      try:
         User.objects.create(id=18,
                             username='pepito',
                             email=self.email,
                             first_name=self.first_name,
                             last_name=self.last_name,
                             phone_number=self.phone_number,
                             password=self.password)
         User.objects.create(id=19,
                             username=username,
                             email=self.email,
                             first_name=self.first_name,
                             last_name=self.last_name,
                             phone_number=self.phone_number,
                             password=self.password)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(User.objects.filter(id=19).first())

   # -----> Email field test <----- #

   def test_email_field_maximum_length_exceeded(self) -> None:
      '''
         Al intentar registrar un usuario con un email que supere los 30 caracteres de longitud "email = Loemipsumdolorsitamet@asdad.com devuelve un ValidationError y no se crea el usuario.
      '''
      self.email = 'Loipsumdoorsitamet@asdasdad.com'
      # When
      error = None
      try:
         User.objects.create(id=18,
                             username=self.username,
                             email=self.email,
                             first_name=self.first_name,
                             last_name=self.last_name,
                             password=self.password)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(User.objects.filter(id=18).first())

#

   def test_email_field_white_space(self) -> None:
      '''
         Al intentar registrar un usuario con un email que contenga espacios en blanco "email =
         Loipsu itamet@asddad.com" devuelve un ValidationError y no se crea el usuario.
      '''
      self.email = 'Loipsum itamet@asddad.com'
      # When
      error = None
      try:
         User.objects.create(id=18,
                             username=self.username,
                             email=self.email,
                             first_name=self.first_name,
                             last_name=self.last_name,
                             password=self.password)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(User.objects.filter(id=18).first())


#

   def test_model_email_field_unique(self) -> None:
      '''
         Al intentar registrar un usuario con un email ya registrado "email =
         itamet@asddad.com" devuelve un ValidationError y no se crea el usuario.
      '''
      email_repeated = 'itamet@asddad.com'
      # When
      error = None
      try:
         User.objects.create(id=18,
                             username=self.username,
                             email='itamet@asddad.com',
                             first_name=self.first_name,
                             last_name=self.last_name,
                             phone_number=self.phone_number,
                             password=self.password)
         User.objects.create(id=19,
                             username=self.username,
                             email=email_repeated,
                             first_name=self.first_name,
                             last_name=self.last_name,
                             phone_number=self.phone_number,
                             password=self.password)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(User.objects.filter(id=19).first())

   # -----> First_name field test <----- #

   def test_model_first_name_fields_maximum_length_exceeded(self) -> None:
      '''
         Al intentar registrar un usuario con un first_name que supere los 25 caracteres de longitud "first_name = Loremipsumdolorsitametasdq" devuelve un ValidationError y no se crea el usuario.
      '''
      self.first_name = 'Loremipsumdolorsitametasdq'
      # When
      error = None
      try:
         User.objects.create(id=18,
                             username=self.username,
                             email=self.email,
                             first_name=self.first_name,
                             last_name=self.last_name,
                             phone_number=self.phone_number,
                             password=self.password)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(User.objects.filter(id=18).first())

   # -----> Last_name field test <----- #

   def test_model_last_name_fields_maximum_length_exceeded(self) -> None:
      '''
         Al intentar registrar un usuario con un first_name que supere los 25 caracteres de longitud "last_name = Loremipsumdolorsitametasdq" devuelve un ValidationError y no se crea el usuario.
      '''
      self.last_name = 'Loremipsumdolorsitametasdq'
      # When
      error = None
      try:
         User.objects.create(id=18,
                             username=self.username,
                             email=self.email,
                             first_name=self.first_name,
                             last_name=self.last_name,
                             phone_number=self.phone_number,
                             password=self.password)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(User.objects.filter(id=18).first())

   # -----> Phone_number field test <----- #

   def test_model_phone_number_fields_maximum_length_exceeded(self) -> None:
      '''
         Al intentar registrar un usuario con un first_name que supere los 8 caracteres de longitud "phone_number = 123456789" devuelve un ValidationError y no se crea el usuario.
      '''
      self.phone_number = '123456789'
      # When
      error = None
      try:
         User.objects.create(id=18,
                             username=self.username,
                             email=self.email,
                             first_name=self.first_name,
                             last_name=self.last_name,
                             phone_number=self.phone_number,
                             password=self.password)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(User.objects.filter(id=18).first())

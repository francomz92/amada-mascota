from logging import error
from django.core.exceptions import ValidationError
from django.utils.timezone import now, timedelta
from django.test import TestCase
from apps.usuario.models import User
from apps.models import Mascota, Publicacion, Ubicacion

### ========== Publicación Model ========== ###


class PublicacionModelTest(TestCase):
   def setUp(self) -> None:
      self.mascota = Mascota.objects.create(nombre='Pepe',
                                            especie='Loro',
                                            raza='Pelicano',
                                            tamano='Grande',
                                            sexo='Macho')
      self.ubicacion = Ubicacion.objects.create(localidad='Avia Terai', barrio='B° 20 viv')
      self.usuario = User.objects.create(username='Joselito',
                                         email='joselito@mail.com',
                                         first_name='Jose',
                                         last_name='Lopez',
                                         phone_number='123456',
                                         password='12345678')
      self.publicacion = Publicacion.objects.create(id=1,
                                                    id_mascota=self.mascota,
                                                    id_usuario=self.usuario,
                                                    id_ubicacion=self.ubicacion)
      return super().setUp()

   def tearDown(self) -> None:
      self.publicacion.delete()
      return super().tearDown()

   # -----> Renovar_fecha_vencimiento method test <----- #

   def test_model_method_renovar_fecha_vencimiento(self):
      '''
         Al llamar al metodo renovar_fecha_vencimiento() se setea una nueva fecha de vencimiento 7 dias posterior a la actual Fecha(yyyy/mm/dd):
      '''
      date = now().date() + timedelta(days=7)
      # When
      self.publicacion.renovar_fecha_vencimiento()
      # Then
      self.assertEqual(self.publicacion.valido_hasta, date)

   # -----> Set_fecha_entrega method test <----- #

   def test_model_method_set_fecha_entrega(self):
      '''
         Al llamar al metodo set_fecha_entrega se setea una fecha de entrega correspondiente a la actual Fecha(yyyy/mm/dd) y se anula la fecha de vencimiento:
      '''
      date = now().date()
      # When
      self.publicacion.set_fecha_entrega()
      # Then
      self.assertEqual(self.publicacion.fecha_entrega, date)
      self.assertEqual(self.publicacion.valido_hasta, None)


### ========== Mascota Model ========== ###


class MascotaModelTest(TestCase):

   # -----> Test setting <----- #

   def setUp(self) -> None:
      self.nombre = 'Mascota'
      self.especie = 'Perro'
      self.raza = 'Caniche'
      self.tamano = 'Chico'
      self.sexo = 'Macho'
      self.otro_dato = 'Lorem Ipsum'
      return super().setUp()

   # -----> Nombre field test <----- #

   def test_model_nombre_field_maximum_length_exceeded(self):
      '''
         Al intentar registrar una mascota con un nombre que supere los 30 caracteres de longitud "nombre = Loremdipsumsdolor sitdaametasco" devuelve un ValidationError y el registro no se crea.
      '''
      nombre = 'Loremdipsumsdolor sitdaametasco'
      # When
      error = None
      try:
         Mascota.objects.create(id=18,
                                nombre=nombre,
                                especie=self.especie,
                                raza=self.raza,
                                tamano=self.tamano,
                                sexo=self.sexo,
                                otro_dato=self.otro_dato)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Mascota.objects.filter(id=18).first())
#

   def test_model_nombre_field_default_nombre(self):
      '''
         Al registrar una mascota sin nombre se le asigna automaticamente "Desconocido" al crearse el registro.
      '''
      # When
      registro = Mascota.objects.create(id=18,
                                        nombre='',
                                        especie=self.especie,
                                        raza=self.raza,
                                        tamano=self.tamano,
                                        sexo=self.sexo,
                                        otro_dato=self.otro_dato)
      # Then
      self.assertIsNotNone(registro.nombre)
      self.assertEqual(registro.nombre, 'Desconocido')

# -----> Especie field test <----- #

   def test_model_especie_field_maximum_length_exceeded(self):
      '''
         Al intentar registrar una mascota de una especie que supere los 7 caracteres de longitud "especie = Mamíferos" devuelve un ValidationError y el registro no se crea.
      '''
      especie = 'Mamíferos'
      # When
      error = None
      try:
         Mascota.objects.create(id=18,
                                nombre=self.nombre,
                                especie=especie,
                                raza=self.raza,
                                tamano=self.tamano,
                                sexo=self.sexo,
                                otro_dato=self.otro_dato)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Mascota.objects.filter(id=18).first())
#

   def test_model_especie_field_invalid_select_option(self):
      '''
         Al intentar registrar una mascota con una especie que no se encuentre en la lista "especie = Cerdo" devuelve un ValidationError y el registro no se crea.
      '''
      especie = 'Cerdo'
      # When
      error = None
      try:
         Mascota.objects.create(id=18,
                                nombre=self.nombre,
                                especie=especie,
                                raza=self.raza,
                                tamano=self.tamano,
                                sexo=self.sexo,
                                otro_dato=self.otro_dato)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Mascota.objects.filter(id=18).first())

# -----> Raza field test <----- #

   def test_model_raza_field_maximum_length_exceeded(self):
      '''
         Al intentar registrar una mascota de una raza que supere los 40 caracteres de logintud "raza = 
         Lorem ipsum dolor sit amets consectetuert" devuelve un ValidationError y el registro no se crea.
      '''
      raza = 'Lorem ipsum dolor sit amets consectetuert'
      # When
      error = None
      try:
         Mascota.objects.create(id=18,
                                nombre=self.nombre,
                                especie=self.especie,
                                raza=raza,
                                tamano=self.tamano,
                                sexo=self.sexo,
                                otro_dato=self.otro_dato)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Mascota.objects.filter(id=18).first())

# -----> Tamano field test <----- #

   def test_model_tamano_field_maximum_length(self):
      '''
         Al intentar registrar una mascota con un tamaño superando los 7 caracteres de longitud "longitud = Gigantesco" devuelve un ValidationError y el registro no se crea.
      '''
      tamano = 'Gigantesco'
      # When
      error = None
      try:
         Mascota.objects.create(id=18,
                                nombre=self.nombre,
                                especie=self.especie,
                                raza=self.raza,
                                tamano=tamano,
                                sexo=self.sexo,
                                otro_dato=self.otro_dato)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Mascota.objects.filter(id=18).first())
#

   def test_model_tamano_field_invalid_select_option(self):
      '''
         Al intentar registrar una mascota con un tamaño que no se encuentre en la lista "tamano = Enorme" devuelve un ValidationError y el registro no se crea.
      '''
      tamano = 'Enorme'
      # When
      error = None
      try:
         Mascota.objects.create(id=18,
                                nombre=self.nombre,
                                especie=self.especie,
                                raza=self.raza,
                                tamano=tamano,
                                sexo=self.sexo,
                                otro_dato=self.otro_dato)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Mascota.objects.filter(id=18).first())

# -----> Sexo field test <----- #

   def test_model_sexo_field_maximum_length(self):
      '''
         Al intentar registrar una mascota de un sexo que no se encuentre en la lista "sexo = Loremsi" devuelve un ValidationError y el registro no se crea.
      '''
      sexo = 'Loremsi'
      # When
      error = None
      try:
         Mascota.objects.create(id=18,
                                nombre=self.nombre,
                                especie=self.especie,
                                raza=self.raza,
                                tamano=self.tamano,
                                sexo=sexo,
                                otro_dato=self.otro_dato)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Mascota.objects.filter(id=18).first())

#

   def test_model_sexo_field_invalid_select_option(self):
      '''
         Al intentar registrar una mascota con un sexo que no se encuentre en la lista "sexo = Otro" devuelve un ValidationError y el registro no se crea.
      '''
      sexo = 'Otro'
      # When
      error = None
      try:
         Mascota.objects.create(id=18,
                                nombre=self.nombre,
                                especie=self.especie,
                                raza=self.raza,
                                tamano=self.tamano,
                                sexo=sexo,
                                otro_dato=self.otro_dato)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Mascota.objects.filter(id=18).first())


### ========== Ubicacion Model ========== ###


class UbicacionModelTest(TestCase):

   # -----> Test setting <----- #

   def setUp(self) -> None:
      self.localidad = 'Avia Terai'
      self.barrio = 'Libertad'
      self.calle = 'Siempreviva'
      self.numero = '123'
      self.entre_calles = 'San Justo - Pasagales'
      self.referencia = 'A tres casas hacia el sur de la carniceria Don Tito'
      return super().setUp()

   # -----> Localidad field test <----- #

   def test_model_localidad_field_invalid_select_option(self):
      '''
         Al intentar registrar una ubicacion con una localidad que no se encuentre en la lista "localidad = Castelli" devuelve un ValidationError y el registro no se crea.
      '''
      localidad = 'Castelli'
      # When
      error = None
      try:
         Ubicacion.objects.create(id=18,
                                  localidad=localidad,
                                  barrio=self.barrio,
                                  calle=self.calle,
                                  numero=self.numero,
                                  entre_calles=self.entre_calles,
                                  referencia=self.referencia)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Ubicacion.objects.filter(id=18).first())

   # -----> Barrio field test <----- #

   def test_model_barrio_field_maximum_length_exceeded(self):
      '''
         Al intentar registrar una ubicacion con una barrio que supere los 50 caracteres de longitud "barrio = Lorem ipsum dolor sit amets consectetuer adipiscing" devuelve un ValidationError y el registro no se crea.
      '''
      barrio = 'Lorem ipsum dolor sit amets consectetuer adipiscing'
      # When
      error = None
      try:
         Ubicacion.objects.create(id=18,
                                  localidad=self.localidad,
                                  barrio=barrio,
                                  calle=self.calle,
                                  numero=self.numero,
                                  entre_calles=self.entre_calles,
                                  referencia=self.referencia)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Ubicacion.objects.filter(id=18).first())

   # -----> Calle field test <----- #

   def test_model_calle_field_maximum_length_exceeded(self):
      '''
         Al intentar registrar una ubicacion con una calle que supere los 50 caracteres de longintud "calle = Lorem ipsum dolor sit amets consectetuer adipiscing" devuelve un ValidationError y el registro no se crea.
      '''
      calle = 'Lorem ipsum dolor sit amets consectetuer adipiscing'
      # When
      error = None
      try:
         Ubicacion.objects.create(id=18,
                                  localidad=self.localidad,
                                  barrio=self.barrio,
                                  calle=calle,
                                  numero=self.numero,
                                  entre_calles=self.entre_calles,
                                  referencia=self.referencia)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Ubicacion.objects.filter(id=18).first())

   # -----> Numero field test <----- #

   def test_model_numero_field_maximum_length_exceeded(self):
      '''
         Al intentar registrar una ubicacion con un numero de más de 5 digitos "numero = 123456" devuelve un ValidationError y el registro no se crea.
      '''
      numero = '123456'
      # When
      error = None
      try:
         Ubicacion.objects.create(id=18,
                                  localidad=self.localidad,
                                  barrio=self.barrio,
                                  calle=self.calle,
                                  numero=numero,
                                  entre_calles=self.entre_calles,
                                  referencia=self.referencia)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Ubicacion.objects.filter(id=18).first())

   # -----> Entre_calles field test <----- #

   def test_model_entre_calles_field_maximum_length_exceeded(self):
      '''
         Al intentar registrar una ubicacion con entre callles que supere los 50 caracteres de longitud "entre_calles = Lorem ipsum dolor sit amets consectetuer adipiscing" devuelve un ValidationError y el registro no se crea.
      '''
      entre_calles = 'Lorem ipsum dolor sit amets consectetuer adipiscing'
      # When
      error = None
      try:
         Ubicacion.objects.create(id=18,
                                  localidad=self.localidad,
                                  barrio=self.barrio,
                                  calle=self.calle,
                                  numero=self.numero,
                                  entre_calles=entre_calles,
                                  referencia=self.referencia)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Ubicacion.objects.filter(id=18).first())

   # -----> Referencia field test <----- #

   def test_model_referencia_field_maximum_length_(self):
      '''
         Al intentar registrar una ubicacion con una referencia que supere los 200 caracteres de lista "referencia = Lorem ipsum dolor sit amet, consectetuer adipiscing elith Aenean commodo ligula eget dolors Aenean massas Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus must Donec qua" devuelve un ValidationError y el registro no se crea.
      '''
      referencia = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elith Aenean commodo ligula eget dolors Aenean massas Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus must Donec qua'
      # When
      error = None
      try:
         Ubicacion.objects.create(id=18,
                                  localidad=self.localidad,
                                  barrio=self.barrio,
                                  calle=self.calle,
                                  numero=self.numero,
                                  entre_calles=self.entre_calles,
                                  referencia=referencia)
      except Exception as err:
         error = err
      # Then
      self.assertEqual(type(error), ValidationError)
      self.assertIsNone(Ubicacion.objects.filter(id=18).first())
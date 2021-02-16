from django.db import models

from datetime import datetime, timedelta

# Create your models here.

listado_ciudades = (('res','resistencia'),('pal','las palmas'))

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    listado_ciudades.append(self)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=4)
    ciudad = models.ForeignKey(
        Ciudad,
        choices=listado_ciudades,
        on_delete=models.RESTRICT,
        on_update=models.RESTRICT)
    descripcion = models.CharField(max_length=50)

class Persona(User):
    direccion = models.OneToOneField(
        Direccion,
        on_delete=models.CASCADE,
        on_update=models.CASCADE) 

lista_especies = (
        ('per','perro'),
        ('gat','gato'),
        ('eri','erizo')
    )

class Animal(models.Model):    
   
    nombre = models.CharField(
        max_length=30,
        default="Desconocido",
        help_text="Indica su nombre, si no lo conoces no te preocupes")
    especie = models.CharField(
        max_length=3,
        choices=lista_especies,
        null=False,
        help_text="Indica su especie")
    fotos = models.ImageField(upload_to ='./media') 
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.especie+'/'+self.nombre

class Mascota(Animal):
    cuidado_especial = models.CharField(max_length=200)
    edad = models.CharField(max_length=2)
    dueño = models.ForeignKey(
        Persona,
        on_update = models.CASCADE,
        on_delete = models.CASCADE)

class Adopcion(models.Model):
    titulo = models.CharField(
        max_length=30,
        help_text="Titulo llamativo para las personas")
    reglas_de_adopcion = models.CharField(
        max_length=200,
        help_text="Bases para poder adoptar")
    animal = models.ForeignKey(
        Animal,
        on_delete=models.CASCADE,
        on_update=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    persona = models.ForeignKey(Persona)

    def __str__(self):
        return self.titulo


opciones_encontrado = (('Si',True),('No',False))
class Perdido(models.Model):
    fecha_hora = models.DateTimeField(auto_now_add=True)
    valido_hasta = models.DateTimeField(default=datetime.now()+timedelta(days=5))
    encontrado = models.CharField(choices=opciones_encontrado)
    fecha_encontrado = models.DateTimeField()
    ultima_ubicacion = models.ForeignKey(Direccion)
    involucrado = models.OneToOneField(Mascota)
    persona = models.ForeignKey(Persona)

opcion = (
        ('Notra','solo lo vi'),
        ('trans','en transito')
    )
class Avistamiento(models.Model):
    
    fecha_hora = models.DateTimeField(auto_now_add=True)
    seleccion = models.CharField(choices=opcion,null=False)
    visto_en = models.ForeignKey(Direccion)
    animal =  models.OneToOneField(Animal)

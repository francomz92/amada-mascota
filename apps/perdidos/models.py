from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Ubicacion(models.Model):
    lista_localidades = (
    ('Avia Terai','Avia Terai'),
    ('Campo Largo','Campo Largo'),
    ('Charata','Charata'),
    ('Colonia Benítez','Colonia Benítez'),
    ('Colonia Elisa','Colonia Elisa'),
    ('Colonias Unida','Colonias Unidas'),
    ('Comandancia Frías','Comandancia Frías'),
    ('Concepción del Bermejo','Concepción del Bermejo'),
    ('Coronel Du Graty','Coronel Du Graty'),
    ('Corzuela','Corzuela'),
    ('El Paranacito','El Paranacito'),
    ('El Sauzalito','El Sauzalito'),
    ('Fortín Belgrano','Fortín Belgrano'),
    ('Gancedo','Gancedo'),
    ('General José de San Martín','General José de San Martín'),
    ('General Pinedo','General Pinedo'),
    ('Hermoso Campo','Hermoso Campo'),
    ('Isla Soto','Isla Soto'),
    ('Juan José Castelli','Juan José Castelli'),
    ('La Clotilde','La Clotilde'),
    ('La Escondida','La Escondida'),
    ('La Leonesa','La Leonesa'),
    ('La Tigra','La Tigra'),
    ('La Verde','La Verde'),
    ('Las Breñas','Las Breñas'),
    ('Las Garcitas','Las Garcitas'),
    ('Las Hacheras','Las Hacheras'),
    ('Las Palmas','Las Palmas'),
    ('Los Frentones','Los Frentones'),
    ('Machagai','Machagai'),
    ('Makallé','Makallé'),
    ('Margarita Belén','Margarita Belén'),
    ('Miraflores','Miraflores'),
    ('Misión Nueva Pompeya','Misión Nueva Pompeya'),
    ('Napenay','Napenay'),
    ('Pampa del Indio','Pampa del Indio'),
    ('Pampa del Infierno','Pampa del Infierno'),
    ('Presidencia de la Plaza','Presidencia de la Plaza'),
    ('Presidencia Roca','Presidencia Roca'),
    ('Puerto Bermejo','Puerto Bermejo'),
    ('Puerto Las Palmas','Puerto Las Palmas'),
    ('Puerto Tirol','Puerto Tirol'),
    ('Quitilipi','Quitilipi'),
    ('San Bernardo','San Bernardo'),
    ('Paraje San Fernando','Paraje San Fernando'),
    ('Santa Sylvina','Santa Sylvina'),
    ('Taco Pozo','Taco Pozo'),
    ('Tres Isletas','Tres Isletas'),
    ('Villa Ángela','Villa Ángela'),
    ('Villa Berthet','Villa Berthet'),
    ('Villa Río Bermejito','Villa Río Bermejito')
    )
    localidad = models.CharField(max_length=30,choices=lista_localidades,null=False)
    barrio = models.CharField(max_length=50,null=False)
    entre_calles = models.CharField(max_length=50,null=True)
    numero = models.CharField(max_length=5,default="S/N")
    calle = models.CharField(max_length=50,null=False)
    otros_datos = models.CharField(max_length=50,default="Sin particular")

    def __str__(self):
        return self.localidad+','+self.barrio+','+self.calle+','+self.numero

class Persona(User):
    pass

class Mascota(models.Model):    
    lista_especies = (
        ('Perro','Perro'),
        ('Gallo','Gallo'),
        ('Gato','Gato'),
        ('Vaca','Vaca'),
        ('Cerdo','Cerdo'),
        ('Pato','Pato'),
        ('Tortuga de tierra','Tortuga de tierra'),
        ('Hámster','Hámster'),
        ('Erizo de tierra','Erizo de tierra')
    )
    sexos = (
    ('Macho','Macho'),
    ('Hembra','Hembra'),
    ('Desconocido','Desconocido'),
    )
    tamanos = (
    ('Enorme','Enorme'),
    ('Grande','Grande'),
    ('Mediano','Mediano'),
    ('Chico','Chico'),
    ('Diminuto','Diminuto'),
    )
    id_dueño = models.ForeignKey(
        Persona,
        default=models.SET_NULL,
        on_delete = models.CASCADE,
        )
    nombre = models.CharField(
        max_length=30,
        default="Desconocido",
        help_text="Indica su nombre si lo conoces",
        )
    familia = models.CharField(max_length=50,default="Desconocido")
    raza = models.CharField(max_length=50,default="Desconocido")
    especie = models.CharField(
        max_length=17,
        choices=lista_especies,
        null=False,
        help_text="Indica la especie")
    edad = models.CharField(max_length=2,default="Desconocido")
    sexo = models.CharField(max_length=11,choices=sexos,null=False)
    fotos = models.ImageField(upload_to ='./media') 
    color = models.CharField(max_length=30,null=True)
    tamaño = models.CharField(max_length=8,choices=tamanos)
    otro_dato = models.CharField(max_length=200,default=models.SET_NULL)

    def __str__(self):
        return self.especie+'-'+self.nombre

class Publicacion(models.Model):
    id_usuario = models.ForeignKey(
        Persona,
        null=False,
        on_delete = models.CASCADE,
        )
    id_mascota = models.ForeignKey(
        Mascota,
        null=False,
        on_delete = models.CASCADE,
    )
    id_ubicacion = models.ForeignKey(
        Ubicacion,
        null=False,
        on_delete = models.DO_NOTHING
    )
    fecha_publicacion = models.DateField(auto_now_add=True)
    fecha_evento = models.DateField(default = datetime.today())
    fecha_entrega = models.DateField(null=True)
    observaciones = models.CharField(max_length=100,default="Sin observaciones")

    def __str__(self):
        #Conformacion del titulo de la publicacion
        especie = Mascota.objects.get(pk=self.id_mascota).only('especie')
        fecha = self.fecha_evento.day+'/'+self.fecha_evento.month
        ubicacion = Ubicacion.objects.get(pk=self.id_ubicacion).only('localidad','barrio')
        return especie+'-'+fecha+'-'+ubicacion
    
    

class Adopcion(models.Model):
    id_publicacion = models.ForeignKey(
        Publicacion,
        null=False,
        on_delete = models.CASCADE
    )
    condicion = models.CharField(max_length=300,default="Cuidar este hermoso ser vivo")

class Perdido(models.Model):
    id_publicacion = models.ForeignKey(
        Publicacion,
        null=False,
        on_delete = models.CASCADE
    )
    gratificacion = models.CharField(max_length=5,default="Sin gratificación")

class Encontro(models.Model):
    en_transito = (
        ('Si','Si'),
        ('No','No'),
    )
    id_publicacion = models.ForeignKey(
            Publicacion,
            null=False,
            on_delete = models.CASCADE
        )
    cuida = models.CharField(max_length=2,choices = en_transito,null=False,help_text="Si tiene el animal y lo cuida indique Si, caso contrario No")
    if cuida == 'Si':
        fecha_limite = models.DateField(null=False,help_text="Si lo cuida,¿hasta cuando lo hara antes de ponerlo en adopción?")
    else:
        fecha_limite = models.DateField(null=True,default=models.SET_NULL)
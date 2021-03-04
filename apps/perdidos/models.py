from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone

global lista_especies
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

global lista_localidades
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

class Ubicacion(models.Model):
    localidad = models.CharField(max_length=30,choices=lista_localidades,null=False)
    barrio = models.CharField(max_length=50,null=False)
    entre_calles = models.CharField(max_length=50,null=True, blank = True)
    numero = models.CharField(max_length=5,default="S/N")
    calle = models.CharField(max_length=50,null=False)
    otros_datos = models.CharField(max_length=50,default="Sin particular")

    def __str__(self):
        return self.localidad+','+self.barrio+','+self.calle+','+self.numero

class Mascota(models.Model):    
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
        User,
        default=None,
        on_delete = models.CASCADE,
        )
    nombre = models.CharField(
        max_length=30,
        default="Desconocido",
        help_text="Indica su nombre si lo conoces"
        )
    familia = models.CharField(max_length=50,default="Desconocido")
    raza = models.CharField(max_length=50,default="Desconocido")
    especie = models.CharField(
        max_length=17,
        choices=lista_especies,
        null=False,
        help_text="Indica la especie")
    edad = models.CharField(max_length=2,default="N")
    sexo = models.CharField(max_length=11,choices=sexos,null=False)
    fotos = models.ImageField(upload_to ='mascota') 
    color = models.CharField(max_length=30,null=True,blank=True)
    tamaño = models.CharField(max_length=8,choices=tamanos)
    otro_dato = models.CharField(max_length=200,null=True, blank= True, default=None)

    def __str__(self):
        return self.especie+'-'+self.nombre

class Notificacion(models.Model):
    tipo_notificacion = (
        ('Adopcion','Adopcion'),
        ('Encontro','Encontro'),
        ('Perdido','Perdio')
    )
    id_usuario = models.ForeignKey(
        User,
        null=False,
        on_delete = models.CASCADE,
        )
    tipo = models.CharField(max_length = 8,choices = tipo_notificacion,null=False)
    especie = models.CharField(max_length = 20,choices=lista_especies,null=False)
    localidad = models.CharField(max_length=30,choices=lista_localidades,null=False)
    fecha_desde = models.DateField(default=timezone.now)
    fecha_hasta = models.DateField(null=False)
    
    def __str__(self):
        return self.id_usuario.last_name+', '+self.id_usuario.first_name+'-'+self.tipo+'-'+self.especie+'-'+self.localidad

class Publicacion(models.Model):
    id_usuario = models.ForeignKey(
        User,
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
    fecha_evento = models.DateField(default=timezone.now)
    fecha_entrega = models.DateField(null=True, blank = True)
    observaciones = models.CharField(max_length=100,default="Sin observaciones")        

    def __str__(self):
        #Conformacion del titulo de la publicacion
        mascota = Mascota.objects.get(pk=self.id_mascota.id)
        fecha = str(self.fecha_evento.day)+'/'+str(self.fecha_evento.month)
        ubicacion =  Ubicacion.objects.get(pk=self.id_ubicacion.id)
        localidad = ubicacion.localidad
        barrio = ubicacion.barrio
        return mascota.especie+' - Fecha: '+fecha+' - '+localidad+', Barrio: '+barrio
    
   #  def save(self,*args,**kwargs):
   #      """Cuando se instancia una publicacion, antes de guardarla, se revisara 
   #      el listado de personas interesadas en el tipo de mascota de la publicacion,
   #      tipo de publicacion y localidad para mostrarle su notificacion personalida"""
   #      e = Mascota.objects.get(pk=self.id_mascota.id)
   #      preferencia_notif_personal = list(Notificacion.objects.filter(tipo = self.__class__.__name__).filter(especie = e.especie).filter(localidad = Ubicacion.objects.get(pk=self.id_ubicacion.id)))
   #      for interesado in preferencia_notif_personal:
   #          nueva_notif_personal  = tiene_notificacion.objects.create(
   #              id_usuario = interesado.id_usuario,
   #              id_publicacion = self.id,
   #              id_notificacion = interesado.id,
   #          )
   #          nueva_notif_personal.save()
   #      return super(Publicacion, self).save( *args, **kwargs)

class Adopcion(Publicacion):
    condicion = models.CharField(max_length=300,default="Cuidar este hermoso ser vivo")

class Perdido(Publicacion):
    gratificacion = models.CharField(max_length=5,default="S/G")

class Encontro(Publicacion):
    en_transito = (
        ('Si','Si'),
        ('No','No'),
    )
    cuida = models.CharField(max_length=2,choices = en_transito,null=False,help_text="Si tiene el animal y lo cuida indique Si, caso contrario No")
    
    #En el admin de Django
    #Esta parte la pruebo y por ej. si selecciona 'Si' ya no funciona porque el formulario ya esta cargado
    #Hay que ver esta funcionalidad, o al seleccionar Recargar el formulario para que tome los cambios.
    if cuida == 'Si':
        fecha_limite = models.DateField(null=False,help_text="Si lo cuida,¿hasta cuando lo hara antes de ponerlo en adopción?")
    else:
        fecha_limite = models.DateField(null=True, blank= True, default=None)

class tiene_notificacion(models.Model):
    id_usuario = models.ForeignKey(
        User,
        null=False,
        on_delete = models.CASCADE,
        )
    id_publicacion = models.ForeignKey(
        Publicacion,
        null=False,
        on_delete = models.CASCADE
    )
    id_notificacion = models.ForeignKey(
        Notificacion,
        null = False,
        on_delete = models.CASCADE
    )
    leido = models.BooleanField(default=False)
    
    def __str__(self):
        x = Notificacion.objects.get(id = self.id_notificacion.id) #.only('tipo','especie')
        return x.tipo+':'+x.especie


        """ tipo,especie = Notificacion.objects.get(id = self.id_notificacion).only('tipo','especie')
        return self.tipo_notificacion+':'+self.especie """
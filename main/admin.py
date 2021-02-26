from django.contrib import admin
from main.models import Contacto 
from apps.perdidos.models import Publicacion, Ubicacion, Mascota, Notificacion,\
Adopcion, Perdido, Encontro, tiene_notificacion

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Ubicacion)
admin.site.register(Mascota)
admin.site.register(Notificacion)
admin.site.register(Publicacion)
admin.site.register(Adopcion)
admin.site.register(Perdido)
admin.site.register(Encontro)
admin.site.register(tiene_notificacion)
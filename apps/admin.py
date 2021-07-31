from apps.models import Mascota, Publicacion, Ubicacion
from django.contrib import admin

# Register your models here.


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'tamano', 'sexo', 'fotos')


@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('localidad', 'barrio')


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_publicacion', 'id_usuario', 'id_mascota', 'id_ubicacion',
                    'valido_hasta', 'fecha_entrega')

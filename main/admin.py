from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User

from main.models import Contacto 
from apps.perdidos.models import Publicacion, Ubicacion, Mascota, Notificacion,\
Adopcion, Perdido, Encontro, tiene_notificacion

# Register your models here.
class MascotaAdmin(admin.ModelAdmin):
    list_display = ["nombre_dueno","nombre", "especie","sexo","foto"]
    list_filter = ["especie"]
    list_filter = ["id_dueño__last_name", "especie"]
    #raw_id_fields= ("id_dueño",)
    search_fields = ["nombre_usuario"]

    def nombre_dueno(self, obj):
        return "%s, %s"%(obj.id_dueño.last_name, obj.id_dueño.first_name)
    nombre_dueno.short_description ="Apellido, Nombre Dueno"

    def foto(self, obj):
        return format_html("<img src={} width=100 height=auto />",obj.fotos.url)


class PerdidoAdmin(admin.ModelAdmin):
    list_display = ["nombre_usuario","nombre_mascota","color_mascota", "foto_mascota", "fecha_publicacion","fecha_evento", "valido_hasta", "gratificacion"]
    list_filter = ["id_usuario__last_name", "id_mascota__color","id_mascota__especie"]
    date_hierarchy = "fecha_publicacion" #filtro avanzado para campo fecha y hora
    ordering=["-fecha_publicacion"]
    
    def nombre_usuario(self, obj):
        return "%s, %s"%(obj.id_usuario.last_name, obj.id_usuario.first_name)
    nombre_usuario.short_description ="Apellido, Nombre Usuario"
    
    def nombre_mascota(self, obj):
        return "%s"%(obj.id_mascota.nombre)
    nombre_mascota.short_description ="Nombre Mascota"

    def color_mascota(self, obj):
        return "%s"%(obj.id_mascota.color)
    color_mascota.short_description ="Color Mascota"
    
    def foto_mascota(self, obj):
        return format_html("<img src=%s width=130 height=auto />"%(obj.id_mascota.fotos.url))
    foto_mascota.short_description ="Foto Mascota"

class EncontradoAdmin(admin.ModelAdmin):
    list_display = ["nombre_usuario","nombre_mascota","color_mascota", "foto_mascota", "fecha_publicacion","fecha_evento", "valido_hasta", "cuida"]
    list_filter = ["id_usuario__last_name", "id_mascota__color","id_mascota__especie"]
    date_hierarchy = "fecha_publicacion" #filtro avanzado para campo fecha y hora
    ordering=["-fecha_publicacion"]

    def nombre_usuario(self, obj):
        return "%s, %s"%(obj.id_usuario.last_name, obj.id_usuario.first_name)
    nombre_usuario.short_description ="Apellido, Nombre Usuario"

    def nombre_mascota(self, obj):
        return "%s"%(obj.id_mascota.nombre)
    nombre_mascota.short_description ="Nombre Mascota"

    def color_mascota(self, obj):
        return "%s"%(obj.id_mascota.color)
    color_mascota.short_description ="Color Mascota"
    
    def foto_mascota(self, obj):
        return format_html("<img src=%s width=130 height=auto />"%(obj.id_mascota.fotos.url))
    foto_mascota.short_description ="Foto Mascota"


class AdopcionAdmin(admin.ModelAdmin):
    list_display = ["nombre_usuario","nombre_mascota","color_mascota", "foto_mascota", "fecha_publicacion","fecha_evento", "valido_hasta", "condicion"]
    list_filter = ["id_usuario__last_name", "id_mascota__color","id_mascota__especie"]
    date_hierarchy = "fecha_publicacion" #filtro avanzado para campo fecha y hora
    ordering=["-fecha_publicacion"]
    
    def nombre_usuario(self, obj):
        return "%s, %s"%(obj.id_usuario.last_name, obj.id_usuario.first_name)
    nombre_usuario.short_description ="Apellido, Nombre Usuario"

    def nombre_mascota(self, obj):
        return "%s"%(obj.id_mascota.nombre)
    nombre_mascota.short_description ="Nombre Mascota"

    def color_mascota(self, obj):
        return "%s"%(obj.id_mascota.color)
    color_mascota.short_description ="Color Mascota"
    
    def foto_mascota(self, obj):
        return format_html("<img src=%s width=130 height=auto />"%(obj.id_mascota.fotos.url))
    foto_mascota.short_description ="Foto Mascota"

class UbicacionAdmin(admin.ModelAdmin):
    list_display = ["localidad","barrio","entre_calles", "numero", "calle","otros_datos"]
    list_filter = ["localidad", "barrio"]
    search_fields=["localidad","barrio"]

class TieneNotificacionAdmin(admin.ModelAdmin):
    list_display = ["nombre_usuario","id_publicacion","datos_notificacion", "leido"]
    list_filter = ["id_usuario__last_name"]
    search_fields=["id_usuario"]

    def nombre_usuario(self, obj):
        return "%s, %s"%(obj.id_usuario.last_name, obj.id_usuario.first_name)
    nombre_usuario.short_description ="Apellido, Nombre Usuario"

    def datos_notificacion(self, obj):
        return "%s - %s - %s "%(obj.id_notificacion.tipo, obj.id_notificacion.especie, obj.id_notificacion.localidad)
    datos_notificacion.short_description ="Notific: Tipo-Especie-Localidad"


class NotificacionAdmin(admin.ModelAdmin):
    list_display = ["nombre_usuario","tipo","especie","fecha_desde", "fecha_hasta"]
    list_filter = ["id_usuario__last_name","tipo", "especie"]
    search_fields=["tipo","especie"]
    
    def nombre_usuario(self, obj):
        return "%s, %s"%(obj.id_usuario.last_name, obj.id_usuario.first_name)
    nombre_usuario.short_description ="Apellido, Nombre Usuario"

admin.site.register(Contacto)
admin.site.register(Ubicacion,UbicacionAdmin)
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Notificacion, NotificacionAdmin)
admin.site.register(Adopcion,AdopcionAdmin)
admin.site.register(Perdido, PerdidoAdmin)
admin.site.register(Encontro, EncontradoAdmin)
admin.site.register(tiene_notificacion,TieneNotificacionAdmin)
#admin.site.register(Publicacion) no debería mostrarse SOLA, ya esta inluido en PERDIDO, ENCONTRO o ADOPCION


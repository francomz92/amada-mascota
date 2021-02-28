from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User
from main.models import Contacto 
from apps.perdidos.models import Publicacion, Ubicacion, Mascota, Notificacion,\
Adopcion, Perdido, Encontro, tiene_notificacion

# Register your models here.
class MascotaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "especie","sexo","id_dueño", "foto"]
    list_filter = ["especie","id_dueño"]
    

    def foto(self, obj):
        return format_html("<img src=%s width=130 height=auto />"%(obj.fotos.url))
 

class PerdidoAdmin(admin.ModelAdmin):
    list_display = ["id_usuario","nombre_mascota","color_mascota", "foto_mascota", "fecha_publicacion","fecha_evento", "gratificacion"]
    list_filter = ["id_usuario__username", "id_mascota__color","id_mascota__especie"]
    date_hierarchy = "fecha_publicacion" #filtro avanzado para campo fecha y hora
    
    def nombre_mascota(self, obj):
        return "%s"%(obj.id_mascota.nombre)
    nombre_mascota.short_description ="Nombre Mascota"

    def color_mascota(self, obj):
        return "%s"%(obj.id_mascota.color)
    color_mascota.short_description ="Color Mascota"
    
    def foto_mascota(self, obj):
        return format_html("<img src=%s width=130 height=auto />"%(obj.id_mascota.fotos.url))
    color_mascota.short_description ="Foto Mascota"

admin.site.register(Contacto)
admin.site.register(Ubicacion)
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Notificacion)
#admin.site.register(Publicacion) no debería mostrarse SOLA, debE ir acOmpañado de PERDIDO, ENCONTRÓ o ADOPCION
admin.site.register(Adopcion)
admin.site.register(Perdido, PerdidoAdmin)
admin.site.register(Encontro)
admin.site.register(tiene_notificacion)
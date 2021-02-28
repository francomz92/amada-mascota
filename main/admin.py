from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User
from main.models import Contacto 
from apps.perdidos.models import Publicacion, Ubicacion, Mascota, Notificacion,\
Adopcion, Perdido, Encontro, tiene_notificacion

# Register your models here.
class MascotaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "especie","sexo","id_dueño", "foto"]
    list_filter = ["especie"]
    raw_id_fields= ("id_dueño",)
    #search_fields = ["id_dueño"]
    #list_filter = ["especie","username"]
    
    def foto(self, obj):
        return format_html("<img src={} width=100 height=auto />",obj.fotos.url)


class PerdidoAdmin(admin.ModelAdmin):
    list_display = ["fecha_publicacion","fecha_evento"]
    list_filter = ["fecha_evento"]
    date_hierarchy = "fecha_publicacion"
    


admin.site.register(Contacto)
admin.site.register(Ubicacion)
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Notificacion)
admin.site.register(Publicacion)
admin.site.register(Adopcion)
admin.site.register(Perdido, PerdidoAdmin)
admin.site.register(Encontro)
admin.site.register(tiene_notificacion)


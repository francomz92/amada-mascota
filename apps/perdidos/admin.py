from django.contrib import admin
from apps.perdidos.models import Perdido

# Register your models here.


@admin.register(Perdido)
class PerdidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_usuario', 'id_mascota', 'fecha_publicacion', 'fecha_perdido',
                    'gratificacion')
    date_hierarchy = 'fecha_perdido'

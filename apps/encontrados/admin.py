from django.contrib import admin
from apps.encontrados.models import Encontro

# Register your models here.


@admin.register(Encontro)
class EncontradoAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'id_mascota', 'fecha_publicacion', 'fecha_encontrado', 'cuida')
    date_hierarchy = 'fecha_encontrado'
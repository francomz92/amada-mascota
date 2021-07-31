from django.contrib import admin
from .models import Adopcion

# Register your models here.


@admin.register(Adopcion)
class AdopcionAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'id_mascota', 'fecha_publicacion', 'condicion')
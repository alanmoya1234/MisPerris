from django.contrib import admin
from core.models import *
# Register your models here.


class MascotaAdmin(admin.ModelAdmin):
    list_filter = ('esterilizado')


admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Tipo_Vivienda)
admin.site.register(Tipo_usuario)
admin.site.register(Usuario)
admin.site.register(Trabajador)
admin.site.register(Login)
admin.site.register(Fondo_Economico)
admin.site.register(Tipo_insumo)
admin.site.register(Transferencia)
admin.site.register(Insumo)
admin.site.register(Refugio)
admin.site.register(Raza)
admin.site.register(Origen_mascota)
admin.site.register(Mascota)
admin.site.register(Visita_Medica)
admin.site.register(Tipo_campania)
admin.site.register(Campania)
admin.site.register(Campania_insumo)
admin.site.register(Visita_adopcion)

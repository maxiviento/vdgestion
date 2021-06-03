from django.contrib import admin
from .models import Solicitante
from .models import Ocupacion
from .models import Salud

#admin.site.register(Solicitante)
#admin.site.register(Ocupacion)
#admin.site.register(Salud)

class SolicitanteAdmin (admin.ModelAdmin):
    list_display = ('nombres', 'apellido', 'sexo')

class OcupacionAdmin(admin.ModelAdmin):
    list_display = ('solicitante', 'ocupacion', 'condicion_laboral', 'frecuencia_laboral', 'ingreso')

class SaludAdmin(admin.ModelAdmin):
    list_display = ('solicitante', 'enfermedad_cronica')

admin.site.register(Solicitante, SolicitanteAdmin)
admin.site.register(Ocupacion, OcupacionAdmin)
admin.site.register(Salud, SaludAdmin)


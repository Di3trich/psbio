from django.contrib import admin
from core.models import Persona, Horario, Registro, Dispositivo, SegmentoHorario, Justificacion, Feriado

admin.site.register(Persona)
admin.site.register(Horario)
admin.site.register(Registro)
admin.site.register(Dispositivo)
admin.site.register(SegmentoHorario)
admin.site.register(Justificacion)
admin.site.register(Feriado)

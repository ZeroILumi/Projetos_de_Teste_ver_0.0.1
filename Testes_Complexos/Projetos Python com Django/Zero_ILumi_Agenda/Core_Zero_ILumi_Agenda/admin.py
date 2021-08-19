from django.contrib import admin
from Core_Zero_ILumi_Agenda.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_do_evento', 'data_da_criacao_do_evento')
    list_filter = ('usuario', 'titulo', 'data_do_evento',)

admin.site.register(Evento, EventoAdmin)
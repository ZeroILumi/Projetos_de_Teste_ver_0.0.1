from django.shortcuts import render, redirect
from zero_ilumi_agenda_core.models import Evento_Agendado


# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def listar_eventos_agendados(request):
    usuario = request.user
    evento = Evento_Agendado.objects.all()
    dados = {'eventos': evento}
    return render(request, 'zero_ilumi_agenda.html', dados)



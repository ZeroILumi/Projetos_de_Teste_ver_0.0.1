from django.shortcuts import render, redirect
from zero_ilumi_agenda_core.models import Evento_Agendado
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('nome_de_usuario')
        password = request.POST.get('senha_do_usuario')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
        else:
            messages.error(request, "Usuário ou Senha Inválidos")
    return redirect('/')


@login_required(login_url='/login/')
def listar_eventos_agendados(request):
    usuario = request.user
    eventos_do_usuario = Evento_Agendado.objects.filter(usuario=usuario)
    dados = {'eventos': eventos_do_usuario}
    return render(request, 'zero_ilumi_agenda.html', dados)


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        usuario = request.user
        titulo = request.POST.get('titulo_agendamento_novo')
        descricao = request.POST.get('input_descricao_agendamento_novo')
        data_do_evento = request.POST.get('data_do_evento_agendamento_novo')
        Evento_Agendado.objects.create(titulo_do_evento_agendado=titulo,
                                       decricao_do_evento_agendado=descricao,
                                       data_do_evento_agendado=data_do_evento,
                                       usuario=usuario)
    return redirect('/')

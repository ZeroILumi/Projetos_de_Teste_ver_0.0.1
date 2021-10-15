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


def logout_user(request):
    logout(request)
    return redirect('/')

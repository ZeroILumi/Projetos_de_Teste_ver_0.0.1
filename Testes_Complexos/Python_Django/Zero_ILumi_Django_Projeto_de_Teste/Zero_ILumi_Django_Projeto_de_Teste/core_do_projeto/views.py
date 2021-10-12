from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(
        '<h1>Hello {nome} com {idade} anos<h1>'.format(nome=nome,
                                                       idade=idade)
    )

def index(request):
    return HttpResponse(
        '<h1>Seja Bem vindo ao Zero ILumi Django Teste 1</h1>'
    )

def soma(request, valor1, valor2):
    resultado_soma = valor1 + valor2
    return HttpResponse(
        '<h1>A Soma: {valor1} + {valor2} = {soma}</h1>'.format(valor1=valor1,
                                                               valor2=valor2,
                                                               soma=resultado_soma)
    )

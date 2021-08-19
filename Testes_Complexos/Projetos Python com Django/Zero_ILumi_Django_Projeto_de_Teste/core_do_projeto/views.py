from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(
        '<h1>Hello {nome} com {idade} anos<h1>'.format(nome=nome,
                                                       idade=idade)
    )

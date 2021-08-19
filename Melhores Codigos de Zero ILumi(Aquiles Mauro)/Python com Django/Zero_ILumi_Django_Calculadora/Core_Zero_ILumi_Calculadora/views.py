from django.shortcuts import render, HttpResponse


# Create your views here.

def index_Zero_ILumi_Calculadora(request):
    return HttpResponse('<h1>Bem Vindo a Calculadora Zero ILumi</h1>')


def soma(request, valor1, valor2):
    resultado_soma = valor1 + valor2
    return HttpResponse(
        '<h1>A Soma: {valor1} + {valor2} = {resultado}</h1>'
        ''.format(valor1=valor1,
                  valor2=valor2,
                  resultado=resultado_soma)
    )


def subtracao(request, valor1, valor2):
    resultado_subtracao = valor1 - valor2
    return HttpResponse(
        '<h1>A Subtração: {valor1} - {valor2} = {resultado}</h1>'
        ''.format(valor1=valor1,
                  valor2=valor2,
                  resultado=resultado_subtracao)
    )


def multiplicacao(request, valor1, valor2):
    resultado_multiplicacao = valor1 * valor2
    return HttpResponse(
        '<h1>A Multiplicação: {valor1} x {valor2} = {resultado}</h1>'
        ''.format(valor1=valor1,
                  valor2=valor2,
                  resultado=resultado_multiplicacao)
    )


def divisao(request, valor1, valor2):
    resultado_divisao = valor1 / valor2
    return HttpResponse(
        '<h1>A Divisão: {valor1} / {valor2} = {resultado}</h1>'
        ''.format(valor1=valor1,
                  valor2=valor2,
                  resultado=resultado_divisao)
    )


def resto_divisao(request, valor1, valor2):
    resultado_resto_divisao = valor1 % valor2
    return HttpResponse(
        '<h1>O Resto da Divisão: {valor1} % {valor2} = {resultado}</h1>'
        ''.format(valor1=valor1,
                  valor2=valor2,
                  resultado=resultado_resto_divisao)
    )

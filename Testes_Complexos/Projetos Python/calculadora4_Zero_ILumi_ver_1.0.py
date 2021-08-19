valor1 = int(input('Digite o Primeiro Valor\n'))
valor2 = int(input('Digite o Segundo Valor\n'))


def soma(valor1, valor2):
    resultado = valor1 + valor2
    return 'Soma: {valor1} + {valor2} = {resultado}'.format(valor1=valor1,
                                                            valor2=valor2,
                                                            resultado=resultado)


def subtracao(valor1, valor2):
    resultado = valor1 - valor2
    return 'Subtração: {valor1} - {valor2} = {resultado}'.format(valor1=valor1,
                                                                 valor2=valor2,
                                                                 resultado=resultado)


def multiplicacao(valor1, valor2):
    resultado = valor1 * valor2
    return 'Multiplicação: {valor1} x {valor2} = {resultado}'.format(valor1=valor1,
                                                                     valor2=valor2,
                                                                     resultado=resultado)


calculadora = {
    'Soma': soma(valor1, valor2),
    'Subtração': subtracao(valor1, valor2),
    'Multiplicação': multiplicacao(valor1, valor2)
}

soma = calculadora['Soma']
subtracao = calculadora['Subtração']

print(soma)
print(subtracao)
# print(multiplicacao)
# print(divisao)
# print(resto_da_divisao)

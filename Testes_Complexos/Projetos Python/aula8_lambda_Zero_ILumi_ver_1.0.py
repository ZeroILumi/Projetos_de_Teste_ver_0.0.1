contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['bode', 'gato', 'tigre', 'leão']

print(contador_letras(lista_animais))

valor1 = int(input('Digite o primero valor\n'))
valor2 = int(input('Digite o segundo valor\n'))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(valor1, valor2))
print(subtracao(valor1, valor2))

calculadora = {
    'Soma':
        lambda a, b: a + b,
    'Subtração':
        lambda a, b: a - b,
    'Multiplicação':
        lambda a, b: a * b,
    'Divisão':
        lambda a, b: a / b,
    'Resto da Divisão':
        lambda a, b: a % b
}

print(type(calculadora))

soma = calculadora['Soma']

print('A Soma: {soma}'.format(soma=soma(10, 10)))

multiplicacao = calculadora['Multiplicação']

print('A Multiplicação: {multiplicacao}'.format(multiplicacao=multiplicacao(10, 10)))
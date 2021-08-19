class Calculadora:

    def __init__(self):
        pass

    def soma_(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao_(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao_(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao_(self, valor_a, valor_b):
        return valor_a / valor_b

    def mod_(self, valor_a, valor_b):
        return valor_a % valor_b


if __name__ == '__main__':
    continua = True
    while continua:
        valor1 = int(input('Digite o primeiro valor:\n'))
        valor2 = int(input('Digite o segundo valor:\n'))
        calculadora = Calculadora()
        print('O Primeiro valor:\n{valor1}'
              ''.format(valor1=valor1))
        print('O Segundo valor:\n{valor2}'
              ''.format(valor2=valor2))
        print('A Soma:\n{valor1} + '
              '{valor2} = '
              '{resultado}'.format(valor1 = valor1,
                              valor2 = valor2,
                              resultado=calculadora.soma_(valor1, valor2)))
        print('A Subtração:\n{valor1} - '
              '{valor2} = '
              '{resultado}'.format(valor1 = valor1,
                                   valor2 = valor2,
                                   resultado=calculadora.subtracao_(valor1, valor2)))
        print('A Multiplicação:\n{valor1} '
              'x {valor2} = '
              '{resultado}'.format(valor1 = valor1, valor2 = valor2, resultado=calculadora.multiplicacao_(valor1, valor2)))
        print('A Divisão:\n{valor1} / '
              '{valor2} = '
              '{resultado}'.format(valor1 = valor1,
                                   valor2 = valor2,
                                   resultado=calculadora.divisao_(valor1, valor2)))
        print('O Resto da Divisão:\n{valor1} % '
              '{valor2} = '
              '{resultado}'.format(valor1 = valor1,
                                   valor2 = valor2,
                                   resultado=calculadora.mod_(valor1, valor2)))
        continuar = int(input('Continuar Calculando\n1:Sim 2:Não\n'))
        while continuar != 1 and continuar != 2:
            continuar = int(input('Digite uma opção valida\n1:Sim 2:Não\n'))
        if continuar == 2:
            continua = False
            print('Obrigado por usar esta calculadora ')


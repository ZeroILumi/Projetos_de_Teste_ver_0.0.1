class Calculadora:

    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma_(self):
        return self.valor_a + self.valor_b

    def subtracao_(self):
        return self.valor_a - self.valor_b


    def multiplicacao_(self):
        return self.valor_a * self.valor_b


    def divisao_(self):
        return self.valor_a / self.valor_b


    def mod_(self):
        return self.valor_a % self.valor_b

if __name__ == '__main__':
    valor1 = int(input('Digite o primeiro valor:\n'))

    valor2 = int(input('Digite o segundo valor:\n'))

    calculadora = Calculadora(valor1, valor2)

    print('O Primeiro valor é:\n{valor1}'
          ''.format(valor1=calculadora.valor_a))

    print('O Segundo valor é:\n{valor2}'
          ''.format(valor2=calculadora.valor_b))

    soma = calculadora.soma_()

    print('A Soma do primeiro valor com'
          'o segundo valor é:\n'
          '{soma}'.format(soma=soma))

    subtracao = calculadora.subtracao_()

    print('A Subtração do primeiro valor com'
          'o segundo valor é:\n'
          '{subtracao}'.format(subtracao=subtracao))

    multiplicacao = calculadora.multiplicacao_()

    print('A Multiplicação do primeiro valor com'
          'o segundo valor é:\n'
          '{multiplicacao}'.format(multiplicacao=multiplicacao))

    divisao = calculadora.divisao_()

    print('A Divisão do primeiro valor com'
          'o segundo valor é:\n'
          '{divisao}'.format(divisao=divisao))

    resto = calculadora.mod_()

    print('O Resto da Divisão do primeiro valor com'
          'o segundo valor é:\n'
          '{resto}'.format(resto=resto))




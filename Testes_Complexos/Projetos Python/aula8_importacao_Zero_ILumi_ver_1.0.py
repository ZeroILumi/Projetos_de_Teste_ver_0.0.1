from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.ligar_ou_desligar()
    print(televisao.ligada)
    valor1 = int(input('Digite o primeiro Valor\n'))
    valor2 = int(input('Digite o segundo Valor\n'))
    calculadora = Calculadora(valor1, valor2)
    print('O Primeiro Valor é:\n{valor1}\n'
          'O Segundo Valor é:\n{valor2}'
          ''.format(valor1 = valor1, valor2 = valor2))
    print('A Soma: {valor1} + {valor2} = {resultado}'.format(valor1 = valor1,
                                                              valor2 = valor2,
                                                              resultado = calculadora.soma_()))
    lista = ['bode', 'cachorro', 'elefante', 'gato']
    print('Total de letras por palavras na lista:\n{total_de_letras}'.format(total_de_letras = contador_letras(lista)))
    print(teste())
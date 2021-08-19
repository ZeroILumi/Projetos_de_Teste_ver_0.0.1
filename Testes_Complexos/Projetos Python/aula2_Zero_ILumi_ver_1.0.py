if __name__ == '__main__':
    a = int(input('Entre com o primeiro valor numerico:\n'))
    b = int(input('Entre com o segundo valor numerico:\n'))
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    resto = a % b

    print('Soma: {} Subtração: {}'.format(soma, subtracao))
    resultado = ('Soma: {soma}. '
                 '\nSubtração: {sub}. '
                 '\nMultiplicação: {multi}.'
                 '\nDivisão: {divisao}.'
                 '\nResto: {resto}'.format(sub=subtracao,
                                           soma=soma,
                                           multi=multiplicacao,
                                           divisao=int(divisao),
                                           resto=resto))

    print(resultado)

    # print('Soma: ' + str(soma))
    # print('Subtracao: ' + str(subtracao))
    # print('Multiplicacao: ' + str(multiplicacao))
    # print(('Divisao: ') + str(int(divisao)))
    # print('Resto: ' + str(resto))
    # x = '1'
    # soma2 = int(x) + 1
    # print(soma2)

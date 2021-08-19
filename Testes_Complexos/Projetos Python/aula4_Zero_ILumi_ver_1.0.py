if __name__ == '__main__':
    nota = int(input('Digite uma nota: \n'))
    while nota > 10:
        nota = int(input('Nota Invalida digite um nota de 0 a 10 \n'))
    print('A nota é {nota}'.format(nota=nota))














    # a = 0
    #
    # while a <= 10:
    #     print(a)
    #     a += 1















    # a = int(input('Digite um número: '))
    #
    # for num in range(a+1):
    #     div = 0
    #     for x in range(1, num+1):
    #         mod = num % x
    #         # print('{a} dividido por {x} resta {mod}'.format(a=num, x=x, mod=mod))
    #         if mod == 0:
    #             div += 1
    #
    #     if div == 2:
    #         print('Número {a} é primo pois so e divisivel por si e por 1'.format(a=num))
    #     # else:
    #     #     print('Número {a} não e primo pois e divisivel por numeros que não somente si e 1'.format(a=num))













    # a = int(input('Digite um número: \n'))
    #
    # div = 0
    #
    # for x in range(1, a+1):
    #     mod = a % x
    #     print('{a} dividido por {x} resta {mod}'.format(a=a, x=x, mod=mod))
    #     if mod == 0:
    #         div += 1
    #
    # if div == 2:
    #     print('Número {a} é primo pois so e divisivel por si e por 1'.format(a=a))
    # else:
    #     print('Número {a} não e primo pois e divisivel por numeros que não somente si e 1'.format(a=a))
if __name__ == '__main__':
    a = int(input('Digite a Nota do Primeiro Bimestre: \n'))
    while a > 10:
        a = int(input('Nota do Primeiro Bimestre invalida digite uma nota entre 0 a 10: \n'))
    b = int(input('Digite a Nota do Segundo Bimestre: \n'))
    while b > 10:
        b = int(input('Nota do Segundo Bimestre invalida digite uma nota entre 0 a 10: \n'))
    c = int(input('Digite a Nota do Terceiro Bimestre: \n'))
    while c > 10:
        c = int(input('Nota do Terceiro Bimestre invalida digite uma nota entre 0 a 10: \n'))
    d = int(input('Digite a Nota do Quarto Bimestre: \n'))
    while d > 10:
        d = int(input('Nota do Quarto Bimestre invalida digite uma nota entre 0 a 10: \n'))
    media = (a + b + c + d) / 4
    print('A Media dos Bimestres é {media}'.format(media=media))











    # if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    #     print('A Média dos 4 Bimestres é {media}'.format(media=media))
    # else:
    #     print('Todos os Bimestres devem ter a nota igual ou menor que 10 uma nota digitada é invalida.')












    # a = int(input('Digite o Primeiro Valor: \n'))
    # b = int(input('Digite o Segundo Valor: \n'))
    # mod_a = a % 2
    # mod_b = b % 2
    # if mod_a == 0 or not mod_b > 0:
    #     print('Foi digitado um número par')
    # else:
    #     print('não foi digitado um número par')



    # a = int(input('Digite o Primeiro Valor: \n'))
    # b = int(input('Digite o Segundo Valor: \n'))
    # c = int(input('Digite o Terceiro Valor \n'))
    # if a > b and a > c:
    #     print('{a} é maior que {b} e {c}'.format(a=a, b=b, c=c))
    # elif b > a and b > c:
    #     print('{b} é maior que {a} e {c}'.format(a=a, b=b, c=c))
    # elif c > a and c > b:
    #     print('{c} é maior que {a} e {b}'.format(a=a, b=b, c=c))
    # print('Final do Programa')




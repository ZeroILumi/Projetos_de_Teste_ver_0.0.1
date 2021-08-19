if __name__ == '__main__':
    lista_numero = [4, 80, 50, 10]
    lista_animal = ['bode', 'leao', 'tigre', 'gato', 'lobo', 'arara']
    # print(lista_animal[3])
    lista_animal[5] = 'dragao'

    lista_animal.insert(7, 'arara')

    print(lista_animal)

    tupla = (1, 10, 12, 14)

    print(tupla)

    print(len(tupla))

    print(len(lista_animal))

    tupla_animal = tuple(lista_animal)

    print(type(tupla_animal))

    print(tupla_animal)

    lista_numerica = list(tupla)

    print(type(lista_numerica))

    lista_numerica[0] = 100

    print(lista_numerica)









    # lista_numero.sort()
    #
    # lista_animal.sort()
    #
    # print(lista_numero)

    # lista_numero.reverse()
    #
    # print(lista_numero)
    #
    # print(lista_animal)
    #
    # lista_animal.reverse()
    #
    # print(lista_animal)















    # animal_vericacao_e_insercao = 'lobo'
    #
    # if animal_vericacao_e_insercao in lista_animal:
    #     print(f'Existe {animal_vericacao_e_insercao} na lista de animais'.format(
    #         animal_vericacao
    #         =
    #         animal_vericacao_e_insercao))
    # else:
    #     print(f'Não existe um {animal_vericacao_e_insercao} na lista de animais.'
    #           f'Sera Incluido.'.format(
    #         animal_vericacao
    #         =
    #         animal_vericacao_e_insercao))
    #     lista_animal.append(animal_vericacao_e_insercao)
    #     print(f'Foi adicionado o {animal_vericacao_e_insercao}.'
    #           f'\nNova Lista:'.format(animal_vericacao_e_insercao
    #                                   =
    #                                   animal_vericacao_e_insercao))
    #     for x in lista_animal:
    #         print(x)
    # lista_animal.pop(lista_animal.index(animal_vericacao_e_insercao))
    # lista_animal.remove(animal_vericacao_e_insercao)
    # print(f'{animal_vericacao_e_insercao} '
    #       f'foi removido da lista de animais'.format(animal_vericacao_e_insercao
    #                                                  =
    #                                                  animal_vericacao_e_insercao))
    # for x in lista_animal:
    #     print(x)

    # nova_lista_animal = lista_animal * 3
    # print(nova_lista_animal)


    # animal_vericacao = 'gato'
    #
    # if animal_vericacao in lista_animal:
    #     print(f'existe {animal_vericacao} na lista de animais'.format(
    #         animal_vericacao
    #         =
    #         animal_vericacao))
    # else:
    #     print(f'não existe um {animal_vericacao} na lista de animais'.format(
    #         animal_vericacao
    #         =
    #         animal_vericacao))


    # print(min(lista_animal))
    # print(max(lista_animal))
    # print(min(lista_numero))
    # print(max(lista_numero))
    # print(sum(lista_numero))


    # soma = 0
    #
    # for x in lista_numero:
    #     print(x)
    #     soma += x
    # print(soma)

    # for x in lista_animal:
    #     print(x)

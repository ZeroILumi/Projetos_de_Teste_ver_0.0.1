def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade_de_letras = len(x)
        contador.append('{nome} tem '
                        '{quantidade_de_letras} letras'.format(nome = x,
                                                               quantidade_de_letras = quantidade_de_letras
                                                               ).capitalize())
    return contador

def teste():
    return 'teste.txt'

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))
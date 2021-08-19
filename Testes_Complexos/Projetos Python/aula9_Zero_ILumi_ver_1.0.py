import shutil



def criar_arquivo(nome_do_arquivo_novo,
                  primeira_linha_do_arquivo_novo):
    diretorio = '{nome_do_arquivo}'.format(
        nome_do_arquivo=nome_do_arquivo_novo)
    arquivo = open(diretorio, 'w')
    arquivo.write('{primeira_linha}'.format(primeira_linha=primeira_linha_do_arquivo_novo))

    print('arquivo criado com sucesso'.title())

    arquivo.close()


def atualizar_arquivo(nome_do_arquivo_a_ser_atualizado,
                      texto_a_ser_escrito_na_proxima_linha):
    diretorio = '{nome_do_arquivo}'.format(
        nome_do_arquivo=nome_do_arquivo_a_ser_atualizado)
    arquivo = open(diretorio, 'a')

    arquivo.write('{texto}'.format(texto=texto_a_ser_escrito_na_proxima_linha))

    print('arquivo atualizado com sucesso'.title())

    arquivo.close()


def ler_arquivo(nome_do_arquivo_a_ser_lido):
    diretorio = '{nome_do_arquivo}'.format(
        nome_do_arquivo=nome_do_arquivo_a_ser_lido)

    arquivo = open(diretorio, 'r')

    texto_do_arquivo = arquivo.read()

    print('conteúdo do arquivo lido:'.title(), '\n{texto_do_arquivo}'.format(texto_do_arquivo=texto_do_arquivo))


def media_notas(nome_do_arquivo_com_as_notas):
    arquivo = open(file=nome_do_arquivo_com_as_notas, mode='r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for nota in aluno_nota:
        lista_notas = nota.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print('A Nota do Aluno {aluno} é: {media}'.format(aluno=aluno,
                                                          media=media(lista_notas)))
        dicionario_de_medias = {
            'Aluno': aluno,
            'Media': media(lista_notas)
        }
        lista_media.append(dicionario_de_medias['Aluno'])
        lista_media.append(dicionario_de_medias['Media'])
    return lista_media
        # Forma 2
        # aluno = lista_notas[0]
        # print(aluno)
        # media = (int(lista_notas[1]) + int(lista_notas[2]) + int(lista_notas[3]) + int(lista_notas[4]))/4
        # print('A Media do Aluno {aluno} é: {media}'.format(aluno=aluno, media=media))

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/Usuario/Desktop/Anime/Downloads')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/Usuario/Desktop/Anime/Downloads')


if __name__ == '__main__':
    # move_arquivo('notas.txt')
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # atualizar_arquivo(nome_do_arquivo_a_ser_atualizado='notas.txt',
    #                   texto_a_ser_escrito_na_proxima_linha='\n{lista_media}\n'.format(lista_media=lista_media))
    # criar_arquivo('teste.txt', 'Primeira Linha.\n')
    aluno = 'Cesar,10,10,4,7'
    # atualizar_arquivo('notas.txt', '\n{aluno}\n'.format(aluno=aluno))
    # ler_arquivo('teste.txt')

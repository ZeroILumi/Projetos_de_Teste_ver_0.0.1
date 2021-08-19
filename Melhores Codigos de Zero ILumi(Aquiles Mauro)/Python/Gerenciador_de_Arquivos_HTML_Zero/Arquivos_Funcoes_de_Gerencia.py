import os


def criar_pasta_area_de_trabalho(nome_da_pasta_nova):
    diretorio = '{nome_da_pasta}'.format(nome_da_pasta=nome_da_pasta_nova)
    diretorio_caminho = 'C:/Users/Usuario/Desktop/{nome_da_pasta}'.format(nome_da_pasta=nome_da_pasta_nova)
    caminho = os.path.join(diretorio, diretorio_caminho)
    modo = 0o177
    try:
        os.mkdir(caminho, modo)
    except OSError:
        print('Não foi possivel criar a Pasta {nome_da_pasta} na area de trabalho'.format(
            nome_da_pasta=nome_da_pasta_nova))
    else:
        print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=nome_da_pasta_nova))

def criar_pasta(nome_da_pasta_nova, nome_da_pasta_area_de_trabalho):
    diretorio = '{nome_da_pasta}'.format(nome_da_pasta=nome_da_pasta_nova)
    diretorio_caminho = 'C:/Users/Usuario/Desktop/{nome_da_pasta_area_de_trabalho}/{nome_da_pasta}'.format(
        nome_da_pasta=nome_da_pasta_nova, nome_da_pasta_area_de_trabalho=nome_da_pasta_area_de_trabalho)
    caminho = os.path.join(diretorio, diretorio_caminho)
    modo = 0o166
    try:
        os.mkdir(caminho, modo)
    except OSError:
        print('Não foi possivel criar a Pasta {nome_da_pasta}'.format(nome_da_pasta=nome_da_pasta_nova))
    else:
        print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=nome_da_pasta_nova))



def criar_arquivo(nome_do_arquivo_novo,
                  primeira_linha_do_arquivo_novo,
                  diretorio_raiz):
    diretorio = '{diretorio_raiz}/{nome_do_arquivo}'.format(diretorio_raiz=diretorio_raiz,
                                                            nome_do_arquivo=nome_do_arquivo_novo)
    arquivo = open(diretorio_raiz, 'w')
    arquivo.write('{primeira_linha}'.format(primeira_linha=primeira_linha_do_arquivo_novo))

    print('arquivo criado com sucesso'.title())

    arquivo.close()


def criar_arquivo_css(nome_do_arquivo_novo, primeira_linha_do_arquivo_novo, diretorio_raiz):
    diretorio = '{diretorio_raiz}/{nome_do_arquivo}'.format(diretorio_raiz=diretorio_raiz,
                                                            nome_do_arquivo=nome_do_arquivo_novo)
    arquivo = open(diretorio, 'w')
    arquivo.write('{primeira_linha}'.format(primeira_linha=primeira_linha_do_arquivo_novo))

    arquivo.close()


def atualizar_arquivo(nome_do_arquivo_a_ser_atualizado,
                      texto_a_ser_escrito_na_proxima_linha):
    diretorio = 'C:/Users/Usuario/Desktop/ArquivosPythonZero/{nome_do_arquivo}'.format(
        nome_do_arquivo=nome_do_arquivo_a_ser_atualizado)
    arquivo = open(diretorio, 'a')

    arquivo.write('{texto}'.format(texto=texto_a_ser_escrito_na_proxima_linha))

    print('arquivo atualizado com sucesso'.title())

    arquivo.close()


def ler_arquivo(nome_do_arquivo_a_ser_lido):
    diretorio = 'C:/Users/Usuario/Desktop/ArquivosPythonZero/{nome_do_arquivo}'.format(
        nome_do_arquivo=nome_do_arquivo_a_ser_lido)

    arquivo = open(diretorio, 'r')

    texto_do_arquivo = arquivo.read()

    print('conteúdo do arquivo lido:'.title(), '\n{texto_do_arquivo}'.format(texto_do_arquivo=texto_do_arquivo))


if __name__ == '__main__':
    # criar_arquivo('teste.txt', 'Primeira Linha.\n')
    # atualizar_arquivo('teste.txt', 'Terceira Linha.\n')
    # ler_arquivo('teste.txt')
    # criar_pasta('Zero')
    criar_arquivo('Zero2', 'Zero222', criar_pasta('a','a'))

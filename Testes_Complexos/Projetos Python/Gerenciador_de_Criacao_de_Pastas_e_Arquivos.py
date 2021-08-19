import os


class Criador_de_pastas_e_arquivos:
    def __init__(self, diretorio_area_de_trabalho, diretorio, arquivo, primeira_linha):
        self.diretorio_area_de_trabalho = diretorio_area_de_trabalho
        self.diretorio = diretorio
        self.arquivo = arquivo
        self.primeira_linha = primeira_linha

    def criar_pasta_area_de_trabalho(self):
        diretorio = '{nome_da_pasta}'.format(nome_da_pasta=self.diretorio_area_de_trabalho)
        diretorio_caminho = 'C:/Users/Usuario/Desktop/{nome_da_pasta}'.format(
            nome_da_pasta=self.diretorio_area_de_trabalho)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o177
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta} na area de trabalho'
                  ' possivelmente ela ja existe.'.format(
                nome_da_pasta=self.diretorio_area_de_trabalho))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=self.diretorio_area_de_trabalho))

    def criar_pasta(self):
        diretorio = self.diretorio
        diretorio_caminho = 'C:/Users/Usuario/Desktop/{diretorio_area_de_trabalho}/{diretorio}'.format(
            diretorio_area_de_trabalho=self.diretorio_area_de_trabalho, diretorio=self.diretorio)
        caminho = os.path.join(diretorio, diretorio_caminho)
        modo = 0o166
        try:
            os.mkdir(caminho, modo)
        except OSError:
            print('Não foi possivel criar a Pasta {nome_da_pasta}'
                  ' possivelmente ela ja existe.'.format(nome_da_pasta=self.diretorio))
        else:
            print('Pasta {nome_da_pasta} criada com sucesso'.format(nome_da_pasta=self.diretorio))

    def criar_arquivo(self):
        diretorio = 'C:/Users/Usuario/Desktop/{diretorio_area_de_trabalho}/{diretorio}/{arquivo}'.format(
            diretorio_area_de_trabalho=self.diretorio_area_de_trabalho, diretorio=self.diretorio, arquivo=self.arquivo)
        arquivo = open(diretorio, 'w')
        arquivo.write('{primeira_linha}'.format(primeira_linha=self.primeira_linha))
        print('arquivo criado com sucesso'.title())
        arquivo.close()

    def ler_arquivo(self):
        diretorio = 'C:/Users/Usuario/Desktop/{diretorio_area_de_trabalho}/{diretorio}/{arquivo}'.format(
            diretorio_area_de_trabalho=self.diretorio_area_de_trabalho, diretorio=self.diretorio, arquivo=self.arquivo)
        arquivo = open(diretorio, 'r')

        texto_do_arquivo = arquivo.read()

        print('conteúdo do arquivo lido:'.title(), '\n{texto_do_arquivo}'.format(texto_do_arquivo=texto_do_arquivo))

    def atualizar_arquivo(self):
        diretorio = 'C:/Users/Usuario/Desktop/{diretorio_area_de_trabalho}/{diretorio}/{arquivo}'.format(
            diretorio_area_de_trabalho=self.diretorio_area_de_trabalho,
            diretorio=self.diretorio,
            arquivo=self.arquivo)
        arquivo = open(diretorio, 'w')

        arquivo.write('{texto}'.format(texto=self.primeira_linha))

        print('arquivo atualizado com sucesso'.title())

        arquivo.close()


if __name__ == '__main__':
    criador_de_pastas_e_arquivos_Html = Criador_de_pastas_e_arquivos(arquivo='Zero1.html', diretorio='Arquivos_html',
                                                                     diretorio_area_de_trabalho='Zero5',
                                                                     primeira_linha='Zero Aqui')
    criador_de_pastas_e_arquivos_Html.criar_pasta_area_de_trabalho()
    criador_de_pastas_e_arquivos_Html.criar_pasta()
    criador_de_pastas_e_arquivos_Html.criar_arquivo()
    criador_de_pastas_e_arquivos_Html.ler_arquivo()

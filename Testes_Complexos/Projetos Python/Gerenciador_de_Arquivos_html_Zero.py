from Arquivos_Funcoes_de_Gerencia import ler_arquivo, criar_arquivo, atualizar_arquivo, criar_arquivo_css

if __name__ == '__main__':
    print('Bem Vindo ao Gerenciador de Arquivos Zero')
    sair = 0
    while sair == 0:
        opcao_escolhida = int(input('Opções\n'
                                    '1: Ler Arquivo HTML\n'
                                    '2: Criar Arquivo HTML\n'
                                    '3: Atualizar Arquivo HTML\n'
                                    '4: Sair\n'))
        if opcao_escolhida == 1:
            nome_do_arquivo_Html = input('Digite o nome do arquivo a ser lido\n')
            nome_do_arquivo_Html += '.html'
            ler_arquivo(nome_do_arquivo_Html)
        elif opcao_escolhida == 2:
            nome_do_arquivo_Html = input('Digite o nome do arquivo a ser criado\n')
            nome_do_arquivo_Css = nome_do_arquivo_Html
            nome_do_arquivo_Html += '.html'
            nome_do_arquivo_Css += '.css'
            titulo_do_arquivo_HTML = input('Digite o Titulo de sua pagina HTML\n')
            primeira_tag_do_arquivo = '<!Doctype html>\n' \
                                      '<html>\n' \
                                      '<head>\n' \
                                      ' <title>{titulodoarquivo}</title>\n' \
                                      ' <meta charset= "UTF-8">\n' \
                                      ' <link rel="stylesheet" type="text/css" href="Estilos_dos_meus_codigos_html/{nome_do_arquivo_Css}"\n>' \
                                      '</head>\n' \
                                      '<body>\n' \
                                      ' <!--Imagem de Bem Vindo-->\n' \
                                      ' <img id="imagem_de_bem_vindo" style="-webkit-user-select: none;margin: auto;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;"\n ' \
                                      ' src="https://d3q93wnyp4lkf8.cloudfront.net/revista/post_images/22961/3449b1c950f7bddd8894903e843959b426976122.png?1567792858">\n' \
                                      ' <!--Fim Imagem de Bem Vindo-->\n' \
                                      ' <section>\n' \
                                      '     <header>\n' \
                                      '         <h1 id="Titulo_Principal_da_Pagina">\n' \
                                      '         {titulo_do_arquivo_2}\n' \
                                      '         </h1>\n' \
                                      '     </header>\n' \
                                      ' </section>\n' \
                                      '</body>\n' \
                                      '</html>\n'.format(titulodoarquivo=titulo_do_arquivo_HTML, titulo_do_arquivo_2=titulo_do_arquivo_HTML, nome_do_arquivo_Css = nome_do_arquivo_Css)
            primeira_regra_css = '#imagem_de_bem_vindo{\n' \
                                 'display: block;\n' \
                                 'margin-left: auto;\n' \
                                 'margin-right: auto;\n' \
                                 'height: 250px;\n' \
                                 'width: 500px;\n' \
                                 '}\n' \
                                 '\n' \
                                 '#Titulo_Principal_da_Pagina{\n' \
                                 'text-align:center;\n' \
                                 'font-size:xx-large;\n' \
                                 'font-style:"OLD ENGLISH TEXT MT";\n' \
                                 '}\n'
            criar_arquivo(nome_do_arquivo_Html, primeira_tag_do_arquivo)
            criar_arquivo_css(nome_do_arquivo_Css, primeira_regra_css)
        elif opcao_escolhida == 3:
            nome_do_arquivo_Html = input('Digite o nome do arquivo a ser atualizado\n')
            nome_do_arquivo_Html += '.html'
            nova_tag_do_arquivo = '<'
            nova_tag_do_arquivo += input('Digite o nome da tag de abertura html\n'.title())
            nova_tag_do_arquivo += '>\n'
            conteudo_da_tag = input('Digite o conteudo de sua tag html\n')
            nova_tag_do_arquivo += conteudo_da_tag
            tem_tag_de_fechamento = int(input('Tem tag de fechamento?\n'
                                              '1: Sim\n'
                                              '2: Não\n'))
            if tem_tag_de_fechamento == 1:
                tag_fechamento = '</'
                tag_fechamento += input('Digite o nome da tag de fechamento html\n')
                tag_fechamento += '>'
                nova_tag_do_arquivo += tag_fechamento
            elif tem_tag_de_fechamento != 1:
                while tem_tag_de_fechamento != 1 and tem_tag_de_fechamento != 2:
                    tem_tag_de_fechamento = int(input('Opção invalida'
                                                      'Tem tag de fechamento?\n'
                                                      '1: Sim\n'
                                                      '2: Não\n'))
            elif tem_tag_de_fechamento == 2:
                print('Ok sem tag de fechamento'.title())

        elif opcao_escolhida == 4:
            sair = int(input('Continuar\n'
                             '1: Sim\n'
                             '2: Não\n'))

            while sair != 1 and sair != 2:
                sair = int(input('Digite um opção valida\n'
                                 '1:Para Continuar\n'
                                 '2:Para Sair\n'))
            if sair == 1:
                sair = 0
            elif sair == 2:
                print('Obrigado por usar o Gerenciador de Arquivos Zero')

        sair = int(input('Continuar\n'
                         '1: Sim\n'
                         '2: Não\n'))

        while sair != 1 and sair != 2:
            sair = int(input('Digite um opção valida\n'
                             '1:Para Continuar\n'
                             '2:Para Sair\n'))
        if sair == 1:
            sair = 0
        elif sair == 2:
            print('Obrigado por usar o Gerenciador de Arquivos Zero')

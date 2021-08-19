from Arquivos_Funcoes_de_Gerencia import criar_arquivo, atualizar_arquivo, ler_arquivo

if __name__ == '__main__':
    print('Bem Vindo ao Gerenciador de Arquivos Zero')
    sair = 0
    while sair == 0:
        opcao_escolhida = int(input('Opções\n'
                                    '1: Ler Arquivos\n'
                                    '2: Criar Arquivos\n'
                                    '3: Atualizar Arquivos\n'
                                    '4: Sair\n'))
        if opcao_escolhida == 1:
            nome_do_arquivo = input('Digite o nome do arquivo a ser lido\n')
            nome_do_arquivo += '.txt'
            ler_arquivo(nome_do_arquivo)
        elif opcao_escolhida == 2:
            nome_do_arquivo = input('Digite o nome do arquivo a ser criado\n')
            nome_do_arquivo += '.txt'
            primeira_linha_do_arquivo = input('Digite o estara escrito na primeira linha do arquivo\n')
            criar_arquivo(nome_do_arquivo, primeira_linha_do_arquivo, )
        elif opcao_escolhida == 3:
            nome_do_arquivo = input('Digite o nome do arquivo a ser atualizado\n')
            nome_do_arquivo += '.txt'
            nova_linha_do_arquivo = input('Digite o texto a ser escrito na proxima linha do arquivo\n')
            atualizar_arquivo(nome_do_arquivo,
                              '\n{nova_linha_do_arquivo}'.format(nova_linha_do_arquivo=nova_linha_do_arquivo))
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





lista = [1, 10]
try:
    arquivo = open('Zero.txt', 'r')
    texto = arquivo.read()
    print(f'{texto}\n')
    divisao = 10 / 1
    numero = lista[1]
    # x = z
except ZeroDivisionError:
    print('Não e possivel realizar uma divisão por 0\n')
except ArithmeticError:
    print('Ocorreu um Erro ao Realizar uma Operação Aritmética\n')
except IndexError:
    print('Não existe este indice na lista informada\n')
# except BaseException as ex:
#     print('Erro Generico, Erro: {excecao}'.format(excecao=ex))
except Exception as ex:
    print('Erro Generico, Erro: {excecao}'.format(excecao=ex))
else:
    print('Não ocorreu nem um erro disparando uma exceção\n')
finally:
    print('Sempre Executa se der erro ou não')
    print('Fechando o Arquivo')
    arquivo.close()
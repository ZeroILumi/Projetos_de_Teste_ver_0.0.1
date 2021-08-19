class Error(Exception):
    pass

class Input_Error(Error):
    def __init__(self, message):
        self.message = message



while True:
    try:
        x = int(input('Digite uma nota de 0 a 10: \n'))
        print(x)
        if x > 10:
            raise Input_Error('Nota não pode ser maior que 10.')
        elif x < 0:
            raise Input_Error('Nota não pode ser menor que 0.')
        break
    except ValueError:
        print('Valor Inválido, Deve-se digitar apenas números inteiros.')
    except Input_Error as ex:
        print(ex)



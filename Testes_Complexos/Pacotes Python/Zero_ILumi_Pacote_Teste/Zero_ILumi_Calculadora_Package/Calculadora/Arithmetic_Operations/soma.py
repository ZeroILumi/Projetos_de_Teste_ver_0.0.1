def somar(valor1, valor2):
    resultado = valor1 + valor2
    return 'A Soma: ' \
           '{valor1} + {valor2} = {resultado}' \
           ''.format(valor1=valor1,
                     valor2=valor2,
                     resultado=resultado)

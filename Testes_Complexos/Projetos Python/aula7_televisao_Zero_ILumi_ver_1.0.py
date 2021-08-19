class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1

    def ligar_ou_desligar(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_numero_canal(self):
        if self.ligada:
            if self.canal <= 100:
                self.canal += 1
            else:
                print('Ja esta no canal maximo o canal 100\n'
                      'Para mudar de canal reduza o canal no - ')

    def diminui_numero_canal(self):
        if self.ligada:
            if self.canal > 1:
                self.canal -= 1
            else:
                print('Ja esta no canal minimo o canal 1\n'
                      'Para mudar de canal aumente o canal no + ')

if __name__ == '__main__':
    televisao = Televisao()
    if not televisao.ligada:
        print('A televisão esta desligada')
        ligar = int(input('Ligar?\n1:Ligar\n2:Manter desligada\n'))
        if ligar == 1:
            televisao.ligar_ou_desligar()
            if televisao.ligada:
                print('A televisão esta Ligada')
        if ligar == 2:
            print('A televisão continua desligada')
    print('O canal atual é: {}'.format(televisao.canal))
    televisao.aumenta_numero_canal()
    print('O canal atual é: {}'.format(televisao.canal))
    televisao.diminui_numero_canal()
    televisao.diminui_numero_canal()
    print('O canal atual é: {}'.format(televisao.canal))
from random import randint
import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Seu Chute', size=(39,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(39,10))],
            [sg.Button('Fechar')]
        ]
        # criar uma janela
        self.janela = sg.Window('Chute o número!', layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # receber os valores
                self.evento, self.valores = self.janela.Read()
                # fazer alguma coisa com estes valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto!')
                            break
                        elif int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('PARABÉNS VOCÊ ACERTOU!!')
                            break
                elif self.evento == 'Fechar' or self.evento == exit:
                    self.evento, self.valores, self.janela == WIN_CLOSED
                    self.janela.close()
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()

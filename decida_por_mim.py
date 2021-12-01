import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso não!',
            'Acho que tá na hora certa'
        ]

    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Faça a sua pergunta')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por Mim!')]
        ]
        # criar a janela
        self.janela = sg.Window('Decida por Mim!', layout=layout)
        while True:
            # ler os valores
            self.eventos, self.valores = self.janela.Read()
            # fazer algo com os valores
            if self.eventos == 'Decida por Mim!':
                print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()

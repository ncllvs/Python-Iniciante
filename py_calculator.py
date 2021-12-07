import PySimpleGUI as sg

sg.theme('BluePurple')

# TAMANHO DA TELA
WIN_W = 30  # width = qtd de caracteres (largura)
WIN_H = 50  # height = altura de caracteres

# MENU LAYOUT
menu_layout = [['File', ['Save', 'Exit']],
               ['Tools', ['Waiting']],
               ['Help', ['About']]]

# ELEMENTOS DENTRO DA NOSSA TELA
# row 1
layout = [[sg.Menu(menu_layout)],
          [sg.Input('0', size=(int(WIN_W/2), 1), font=('Consolas', 20), key='-BOX-'),  # visor da calculadora
           sg.Button('<-', font=('Consolas', 20), key='-BACKARROW-'),                  # botão de apagar último
           sg.Button('C', font=('Consolas', 20), key='-CLEAR-')],                      # botão para limpar tudo
# row 2
          [sg.Button('7', font=('Consolas', 20), key='-SEVEN-'),
           sg.Button('8', font=('Consolas', 20), key='-EIGHT-'),
           sg.Button('9', font=('Consolas', 20), key='-NINE-'),
           sg.Button('+', font=('Consolas', 20), key='-PLUS-'),
           sg.Button('*', font=('Consolas', 20), key='-TIMES-')],
# row 3
          [sg.Button('4', font=('Consolas', 20), key='-FOUR-'),
           sg.Button('5', font=('Consolas', 20), key='-FIVE-'),
           sg.Button('6', font=('Consolas', 20), key='-SIX-'),
           sg.Button('-', font=('Consolas', 20), key='-MINUS-'),
           sg.Button('/', font=('Consolas', 20), key='-DIVIDED-')],
# row 4
          [sg.Button('1', font=('Consolas', 20), key='-ONE-'),
           sg.Button('2', font=('Consolas', 20), key='-TWO-'),
           sg.Button('3', font=('Consolas', 20), key='-THREE-'),
           sg.Button('0', font=('Consolas', 20), key='-ZERO-'),
           sg.Button('=', font=('Consolas', 20), key='-RESULT-')]
          ]

# vamos criar uma classe que vai conter nosso app
class App():
    def __init__(self):
        self.window = sg.Window('PyCalculator', layout=layout, margins=(0,0), resizable=True, return_keyboard_events=False)
        self.result = 0
        self.oper = ''
        self.window.read(timeout=1)
        for i in range(1, 5):
            for button in layout[i]:
                button.expand(expand_x=True, expand_y=True)

    # aqui serão definidas as funções do nosso menu_layout
    def about(self):
        sg.popup('About', 'just an example', 'contact me')

    # aqui será definida a função que mostra o resultado no visor da calculadora
    def resulter(self):
        if self.oper == '+':
            return float(self.result) + float(self.values['-BOX-'])
        if self.oper == '-':
            return float(self.result) - float(self.values['-BOX-'])
        if self.oper == '*':
            return float(self.result) * float(self.values['-BOX-'])
        if self.oper == '/':
            return float(self.result) / float(self.values['-BOX-'])

    # aqui será definida a função que mantém nosso programa rodando
    def start(self):
        while True:
            event, self.values = self.window.read()

            if event in (None, 'Exit', sg.WIN_CLOSED):
                break

            # clicando em about no menu, ativa essa função
            if event in ('About'):
                self.about()

            if event in ('-ONE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='1')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '1')
            if event in ('-TWO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='2')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '2')
            if event in ('-THREE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='3')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '3')
            if event in ('-FOUR-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='4')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '4')
            if event in ('-FIVE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='5')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '5')
            if event in ('-SIX-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='6')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '6')
            if event in ('-SEVEN-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='7')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '7')
            if event in ('-EIGHT-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='8')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '8')
            if event in ('-NINE-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='9')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '9')
            if event in ('-ZERO-'):
                if self.values['-BOX-'] == '0':
                    self.window['-BOX-'].update(value='0')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-'] + '0')

            # vamos definir as funções especiais, apagar último C e clear all
            if event in ('-CLEAR-'):
                self.result = 0
                self.window['-BOX-'].update(value=self.result)

            if event in ('-BACKARROW-'):
                self.window['-BOX-'].update(value=self.values['-BOX-'][:-1])

            # vamos definir as funções + - * /
            if event in ('-PLUS-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '+'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')
            if event in ('-MINUS-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '-'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')
            if event in ('-TIMES-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '*'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')
            if event in ('-DIVIDED-'):
                if self.oper != '':
                    self.result = self.resulter()
                else:
                    self.oper = '/'
                    self.result = self.values['-BOX-']
                self.window['-BOX-'].update(value='')
            if event in ('-RESULT-'):
                self.result = self.resulter()
                self.window['-BOX-'].update(value=self.result)
                self.result = 0
                self.oper = ''

App().start()

# Buscador de personagem
import PySimpleGUI as sg

class Personagem:
    def __init__(self):
        self.question1 = 'Estrelas: '
        self.question2 = 'Região: '
        self.question3 = 'Elemento: '
        self.question4 = 'Arma: '
        self.question5 = 'Viajante? '
        self.amenoT5 = ['Kazuha', 'Venti', 'Xiao', 'Jean', 'Viajante']
        self.amenoT4 = ['Sucrose', 'Sayu']
        self.cryoT5 = ['Eula', 'Ayaka', 'Ganyu', 'Qiqi', 'Aloy']
        self.cryoT4 = ['Diona', 'Rosaria', 'Kaeya','Chongyun']
        self.geoT5 = ['Zhongli', 'Albedo', 'Itto', 'Viajante']
        self.geoT4 = ['Gorou', 'Noelle']
        self.pyroT5 = ['Hutao', 'Yoimiya', 'Diluc', 'Klee']
        self.pyroT4 = ['Bennet', 'Xiangling', 'Thoma', 'Yanfei', 'Xinyan', 'Amber']
        self.waterT5 = ['Childe', 'Mona', 'Kokomi']
        self.waterT4 = ['Xingqiu', 'Barbara']
        self.eletroT5 = ['Ei', 'Keqing', 'Viajante']
        self.eletroT4 = ['Beidou', 'Fischl', 'Razor', 'Lisa']
        self.mensagemErro = 'Esta região não possui personagem com este tipo de arma/elemento! '
    
    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Buscador de personagem Genshin Impact')],
            [sg.Output(size=(50,0))],
            [sg.Input(size=(25,0),key='escolha'.lower())],
            [sg.Button('Iniciar')],
            [sg.Button('Buscar')]
        ]

        # criar janela
        self.janela = sg.Window('Personagem',layout=layout)

        # ler os valores
        self.LerValores()

        # fazer algo com os dados
        try:
            if self.evento == 'Iniciar':
                print(self.question1)
                # ESTRELAS
                if self.valores['escolha'] == 'T5':
                    print(self.question2)
                    self.LerValores()
                    # REGIÃO
                    if self.valores['escolha'] == 'mondstadt':
                        print(self.question3)
                        self.LerValores()
                        # ELEMENTO
                        if self.valores['escolha'] == 'ameno':
                            print(self.question4)
                            self.LerValores()
                            # ARMA
                            if self.valores['escolha'] == 'arco':
                                print(self.amenoT5[1])
                            elif self.valores['escolha'] == 'espada':
                                print(self.question5)
                                self.LerValores()
                                # VIAJANTE?
                                if self.valores['escolha'] == 'sim':
                                    print(self.amenoT5[4])
                                else:
                                    print(self.amenoT5[3])
                            else:
                                print(self.mensagemErro)
                        # ELEMENTO
                        elif self.valores['escolha'] == 'cryo':
                            print(self.question4)
                            self.LerValores()
                            # ARMA
                            if self.valores['escolha'] == 'espada':
                                print(self.cryoT5[0])
                            elif self.valores['escolha'] == 'arco':
                                print(self.cryoT5[4])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'geo':
                            print(self.geoT5[1])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'water':
                            print(self.waterT5[1])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'pyro':
                            print(self.question4)
                            self.LerValores()
                            # ARMA
                            if self.valores['escolha'] == 'espada':
                                print(self.pyroT5[2])
                            elif self.valores['escolha'] == 'catalisador':
                                print(self.pyroT5[3])
                            else:
                                print(self.mensagemErro)

                    # REGIÃO
                    elif self.valores['escolha'] == 'liyue':
                        print(self.question3)
                        self.LerValores()
                        # ELEMENTO
                        if self.valores['escolha'] == 'ameno':
                            print(self.amenoT5[2])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'cryo':
                            print(self.question4)
                            self.LerValores()
                            # ARMA
                            if self.valores['escolha'] == 'arco':
                                print(self.cryo[2])
                            elif self.valores['escolha'] == 'catalisador':
                                print(self.cryo[3])
                            else:
                                print(self.mensagemErro)
                        # ELEMENTO
                        elif self.valores['escolha'] == 'geo':
                            print(self.question4)
                            self.LerValores()
                            # ARMA
                            if self.valores['escolha'] == 'lança':
                                print(self.geoT5[0])
                            elif self.valores['escolha'] == 'espada':
                                print(self.geoT5[3])
                            else:
                                print(self.mensagemErro)
                        # ELEMENTO
                        elif self.valores['escolha'] == 'pyro':
                                print(self.pyroT5[0])

                        # ELEMENTO
                        elif self.valores['escolha'] == 'water':
                            print(self.waterT5[0])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'eletro':
                            print(self.eletroT5[1])
                    # REGIÃO
                    elif self.valores['escolha'] == 'inazuma':
                        print(self.question3)
                        self.LerValores()
                        # ELEMENTO
                        if self.valores['escolha'] == 'ameno':
                            print(self.amenoT5[0])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'cryo':
                            print(self.cryoT5[1])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'geo':
                            print(self.geoT5[2])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'pyro':
                            print(self.pyroT5[2])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'water':
                            print(self.geoT5[2])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'eletro':
                            print(self.question4)
                            self.LerValores()
                            # ARMA
                            if self.valores['escolha'] == 'lança':
                                print(self.eletroT5[0])
                            elif self.valores['escolha'] == 'espada':
                                print(self.eletroT5[2])
                # ESTRELAS
                if self.valores['escolha'] == 'T4':
                    print(self.question2)
                    self.LerValores()
                    # REGIÃO
                    if self.valores['escolha'] == 'mondstadt':
                        print(self.question3)
                        self.LerValores()
                        # ELEMENTO
                        if self.valores['escolha'] == 'ameno':
                            print(self.mensagemErro)
                        elif self.valores['escolha'] == 'cryo':
                            print(self.question4)
                            self.LerValores()
                            # ARMA
                            if self.valores['escolha'] == 'arco':
                                print(self.cryoT4[0])
                            elif self.valores['escolha'] == 'lança':
                                print(self.cryoT4[1])
                            elif self.valores['escolha'] == 'espada':
                                print(self.cryoT4[2])
                            else:
                                print(self.mensagemErro)
                        # ELEMENTO
                        elif self.valores['escolha'] == 'geo':
                            print(self.geoT4[1])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'pyro':
                            print(self.question4)
                            self.LerValores()
                            # ARMA
                            if self.valores['escolha'] == 'espada':
                                print(self.pyroT4[0])
                            elif self.valores['escolha'] == 'arco':
                                print(self.pyroT4[5])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'water':
                            print(self.waterT4[1])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'eletro':
                            print(self.question4)
                            self.LerValores()
                            # ARMA
                            if self.valores['escolha'] == 'arco':
                                print(self.eletroT4[1])
                            elif self.valores['escolha'] == 'espada':
                                print(self.eletroT4[2])
                            elif self.valores['escolha'] == 'catalisador':
                                print(self.eletroT4[3])
                            else:
                                print(self.mensagemErro)
                    # REGIÃO
                    elif self.valores['escolha'] == 'liyue':
                        print(self.question3)
                        self.LerValores()
                        # ELEMENTO
                        if self.valores['escolha'] == 'ameno':
                            print(self.amenoT4[0])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'cryo':
                            print(self.cryoT4[3])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'geo':
                            print(self.mensagemErro)
                        # ELEMENTO
                        elif self.valores['escolha'] == 'pyro':
                            print(self.question4)
                            self.LerValores()
                            # ARMA
                            if self.valores['escolha'] == 'lança':
                                print(self.pyroT4[1])
                            elif self.valores['escolha'] == 'catalisador':
                                print(self.pyroT4[3])
                            elif self.valores['escolha'] == 'espadao':
                                print(self.pyroT4[4])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'water':
                            print(self.waterT4[0])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'eletro':
                            print(self.eletroT4[0])
                    # REGIÃO
                    elif self.valores['escolha'] == 'inazuma':
                        print(self.question3)
                        self.LerValores()
                        # ELEMENTO
                        if self.valores['escolha'] == 'ameno':
                            print(self.amenoT4[1])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'cryo':
                            print(self.mensagemErro)
                        # ELEMENTO
                        elif self.valores['escolha'] == 'geo':
                            print(self.geoT4[0])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'pyro':
                            print(self.pyroT4[2])
                        # ELEMENTO
                        elif self.valores['escolha'] == 'water':
                            print(self.mensagemErro)
                        # ELEMENTO
                        elif self.valores['escolha'] == 'eletro':
                            print(self.mensagemErro)
                    # REGIÃO
                    elif self.valores['escolha'] == 'sumaru':
                        print('Essa região ainda não foi desenvolvida!')
            # ESTRELAS
            else:
                print('Opção inválida, tente novamente')
        except:
            print('Algum erro aconteceu')

    def LerValores(self):
            self.evento, self.valores = self.janela.Read()

buscador = Personagem()
buscador.Iniciar()

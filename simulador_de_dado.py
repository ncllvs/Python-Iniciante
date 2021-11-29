# Simulador de dado
# Gerar números de 1 até 6 conforme o funcionamento de um dado

from random import randint
from time import sleep

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Desejas lançar quantos dados? '

    def Iniciar(self):
        while True:
            try:
                resposta = int(input(self.mensagem))
                while resposta <= 0:
                    print('\033[31mValor INVÁLIDO! Digite apenas valores inteiros maiores do que 0!\033[m')
                    resposta = int(input(self.mensagem))
                break
            except:
                print('\033[31mValor INVÁLIDO! Digite apenas valores inteiros!\033[m')
        if resposta > 1:
            print('\033[32mLançando os dados..')
            sleep(3)
            cont = 0
            for c in range(1, resposta + 1):
                valor = randint(self.valor_minimo, self.valor_maximo)
                print(f'O valor do {c}º dado é: {valor}')
                cont += 1
                sleep(0.3)
        else:
            print('\033[32mLançando o dado..')
            sleep(3)
            valor = randint(self.valor_minimo, self.valor_maximo)
            print(f'O valor do dado é: {valor}')

simulador = SimuladorDeDado()
simulador.Iniciar()

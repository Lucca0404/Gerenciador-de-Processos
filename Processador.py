from Processo import Processo
from time import sleep
import threading

class Processador():

    def __init__(self) -> None:
        self.novo : list = []
        self.pronto : list = []
        self.executando : Processo = None

    def inserir(self,processo : Processo) -> None:
        self.pronto.append(processo)
        print(f'O processo {processo.nome} foi adicionado no estado pronto\n')
    
    def executar(self, processo : Processo) -> None:
        if processo in self.pronto:
            if self.executando is None:
                self.executando = processo
                self.pronto.remove(processo)
            else:
                self.pronto.append(self.executando)
                self.executando = processo
                self.pronto.remove(processo)
        print(f'O processo {processo.nome} está no estado executando')
        sleep(0.05)
        g = self.executando.executar()
        try:
            self.executando.indice = next(g)
        except StopIteration:
            print(f'O processo {self.executando.nome} terminou')
            sleep(5)
            self.executando = None
            


                
        
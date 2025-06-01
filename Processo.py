from typing import Callable
import time

class Processo():

    def __init__(self, nome : str, funcao : Callable[[int],int], prioridade : int) -> None:
        self.nome = nome
        self.funcao = funcao
        self.prioridade = prioridade
        self.indice = 0
        self.tempo_inicial = 0

    def executar(self) -> Callable[[int],int]:
        if self.indice == 0:
            self.tempo_inicial = time.perf_counter()
        g = self.funcao(self.indice, self.tempo_inicial)
        return g
        
        
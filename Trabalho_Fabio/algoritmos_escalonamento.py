from Processador import Processador
from Processo import Processo
import time

def escalonamento_prioridade(cpu : Processador):
    chegada = []
    maior_prioridade = float("-inf")
    processo_prioridade = None
    while len(cpu.pronto) > 0 or not cpu.executando is None:
        for proc in cpu.pronto:
            if proc.prioridade > maior_prioridade:
                maior_prioridade = proc.prioridade
                processo_prioridade = proc
        cpu.executar(processo_prioridade)
        if processo_prioridade.indice == 90 and len(chegada) == 0:
            yield [processo_prioridade, chegada]         
        if cpu.executando:
            maior_prioridade = cpu.executando.prioridade
            processo_prioridade = cpu.executando
        else:
            if len(chegada) == 0:
                print(f'E temos o nosso vencedor!!!!!! {processo_prioridade.nome} ganhou!')
                time.sleep(2)
            chegada.append(processo_prioridade)
            maior_prioridade = float('-inf')
            processo_prioridade = None

def round_robin(cpu : Processador, quantu : int):
    chegada = []
    while len(cpu.pronto) > 0 or not cpu.executando is None:
        tempo = 0
        p = cpu.pronto[0]
        cpu.executar(p) 
        while tempo < quantu and not cpu.executando is None:   
            tempo = time.perf_counter()
            cpu.executar(p)  
        
        if cpu.executando is None:
            if len(chegada) == 0:
                print(f'E temos o nosso vencedor!!!!!! {p.nome} ganhou!')
                time.sleep(2)
            chegada.append(p)
        else:
            print('TROCOU!!!!!!!!!!!!')
            time.sleep(0.2)
    return chegada

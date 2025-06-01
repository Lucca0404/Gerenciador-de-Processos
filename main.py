from Processo import Processo
from processos import processo_1, processo_2, processo_3
from Processador import Processador
from time import sleep
import os
from algoritmos_escalonamento import escalonamento_prioridade, round_robin

def main():
    
    cpu = Processador()
    p1 = Processo('sorteador', processo_1, 1)
    p2 = Processo('movedor', processo_2, 2)
    p3 = Processo('contador', processo_3, 3)
    
    print("Bem vindo usuário curioso, aqui você verá como diferentes processos funcionam em algoritmos de escalonamento distintos *_*")
    sleep(5)
    print("Primeiro vamos adicionar alguns processos no nosso processador, isso pode demorar um pouco >_<\n")
    sleep(4)
    os.system('cls')
    for i in range(3):
        print('Loading')
        sleep(0.2)
        os.system('cls')
        print('Loading.')
        sleep(0.2)
        os.system('cls')
        print('Loading..')
        sleep(0.2)
        os.system('cls')
        print('Loading...')
        sleep(0.2)
        os.system('cls')
    cpu.inserir(p1)
    sleep(0.3)
    cpu.inserir(p2)
    sleep(0.3)
    cpu.inserir(p3)
    sleep(2)
    os.system('cls')
    print("Pronto!!!!! agora podemos começar a nossa simulação *.*")
    print('Utilize esse programa com responsabilidade ¬_¬')
    sleep(4)
    os.system('cls')
    while 1:
        print('Menu interativo\nSelecione uma das opções abaixo:\n\n',
        '[1] Ver o tempo de cada processo individualmente\n',
        '[2] Corrida entre os processos! oMo\n')
        entrada = input('')
        match entrada:
            case '1':
                os.system('cls')
                print('Vamos ver o tempo que demora para cada processo rodar na cpu *_*\n')
                lista = cpu.pronto.copy()
                sleep(4)
                for i in lista:
                    print(f'inicando o processo {i.nome}.')
                    sleep(3)
                    cpu.executar(i)
                    while not cpu.executando is None:
                        cpu.executar(i)
                    sleep(5)
                print('UaU, eles executam muito rápido, estou ansioso para ver quem ganhará a corrida!\n')
                sleep(3)
                print('Agora vamos realocar os processos na CPU *_*')
                sleep(3)
                p1 = Processo('sorteador', processo_1, 1)
                p2 = Processo('movedor', processo_2, 2)
                p3 = Processo('contador', processo_3, 3)
                cpu.inserir(p1)
                cpu.inserir(p2)
                cpu.inserir(p3)
                sleep(3)
                print('Perfeito!')
                print('Aperte qualquer botão para voltar para o menu: ')
                espera = input('')
                os.system('cls')
            case '2':
                os.system('cls')
                for i in range(3):
                    print('Loading')
                    sleep(0.2)
                    os.system('cls')
                    print('Loading.')
                    sleep(0.2)
                    os.system('cls')
                    print('Loading..')
                    sleep(0.2)
                    os.system('cls')
                    print('Loading...')
                    sleep(0.2)
                    os.system('cls')
                print("VAI COMEÇAR AGORA MAIS UMA CORRIDA INSANA ENTRE PROCESSOS!!!!!!!!!!!!")
                sleep(4)
                print('Diretamente do terminal da sua IDE favorita, estamos transmitindo a corrida mais esperado das últimas semanas. Aquela que pode ser a corrida mais insignificante da história da computação!!!!')
                sleep(4)
                print('Dentre nossos competidores temos nomes genéricos como:\n')
                sleep(3)
                print('Sorteador!!!!')
                sleep(2)
                print('Movedor!!!!')
                sleep(2)
                print('e Contador!!!!')
                sleep(2)
                print('Quem será que vai ganhar essa corrida? tudo será decidido nos próximos segundos por ninguém mais que você, sim estou falando com você que está lendo esse texto!')
                sleep(5)
                print('Escolha um dos algoritmos de escalonamento abaixo para guiar os nossos participantes durante a corrida:\n')
                print('  [1] Round-Robin\n')
                print('  [2] Escalonamento por prioridade\n')
                entrada = input('')
                match entrada:
                    case '1':
                        os.system('cls')
                        print('Perfeito, você escolheu o algoritmo de round robin!!!')
                        sleep(4)
                        print('Esse algoritmo vai executar os processos com base em um pacote de tempo, ou seja, cada processo vai executar por um tempo e depois dar lugar ao próximo processo!')
                        sleep(5)
                        print('Esse algoritmo sempre deixa as corridas muito interessantes porque não sabemos quem vai ganhar a corrida dependendo do tempo que colocarmos no pacote ^_^')
                        sleep(4)
                        print('Aperte qualquer botão para começar a corrida.')
                        pausa = input('')
                        os.system('cls')
                        print('Escolha o tempo que o pacote terá: ')
                        print(' [1] 1 seg')
                        print(' [2] 0.5 seg')
                        print(' [3] 0.1 seg')
                        entrada = input('')
                        match entrada:
                            case '1':
                                quantu = 1
                            case '2':
                                quantu = 0.5
                            case '3':
                                quantu = 0.1
                            case _:
                                print('Opção inválida, tente 1 ou 2\n')
                                sleep(3)
                                os.system('cls')
                                continue
                        print(f'Perfeito, você escolheu {quantu} segundos!!!')
                        sleep(3)
                        os.system('cls')
                        print('Agora vamos começar a corrida!!!!!')
                        sleep(3)
                        print('Em suas marcas...')
                        sleep(3)
                        os.system('cls')
                        print('COMEÇOU!!!!!!!')
                        sleep(3)
                        ordem = round_robin(cpu, quantu)
                        print('FIM DA CORRIDA!!!')
                        sleep(3)
                        print('A ordem de chegada foi:')
                        lugar = 1
                        for i in ordem:
                            print(f'{lugar}º lugar - {i.nome}')
                            lugar += 1
                            sleep(1)
                        print('Foi uma ótima corrida, mas creio que teremos revanches *_*')
                        sleep(4)
                        print('Vamos realocar os processos.')
                        sleep(2)
                        p1 = Processo('sorteador', processo_1, 1)
                        p2 = Processo('movedor', processo_2, 2)
                        p3 = Processo('contador', processo_3, 3)
                        cpu.inserir(p1)
                        cpu.inserir(p2)
                        cpu.inserir(p3)
                        print('Aperte qualquer coisa para voltar para o menu:')
                        pausa = input('')
                        os.system('cls')
                    case '2':
                        os.system('cls')
                        print('Perfeito, você escolheu o algoritmo de escalonamento por prioridade!!!')
                        sleep(4)
                        print('Esse algoritmo vai executar os processos com base na ordem de prioridade deles, ou seja, o processo de maior prioridade terminará primeiro!')
                        sleep(5)
                        print('Para as coisas ficarem interessantes vou permitir que de vez em quando você mude a prioridade dos processos ^_^')
                        sleep(4)
                        print('Aperte qualquer botão para começar a corrida.')
                        pausa = input('')
                        for i in cpu.pronto:
                            os.system('cls')
                            print('Escolha a prioridade de cada processo:\n')
                            print(f'  Prioridade do {i.nome}: ', end='')
                            p = int(input(''))
                            i.prioridade = p
                        sleep(1)
                        os.system('cls')
                        print('Perfeito as prioridades foram escolhidas!')
                        sleep(3)
                        print('Agora vamos começar a corrida!!!!!')
                        sleep(3)
                        print('Em suas marcas...')
                        sleep(3)
                        os.system('cls')
                        print('COMEÇOU!!!!!!!')
                        sleep(3)
                        g = escalonamento_prioridade(cpu)
                        p = next(g)
                        while True:
                            print(f'Eita, parece que nesse ritmo o {p[0].nome} vai ganhar a corrida *_*')
                            sleep(3)
                            print('Você gostaria de mudar isso trocando a prioridade dos processos?')
                            print(' [1] sim')
                            print(' [2] não')
                            entrada = input('')
                            match entrada:
                                case '1':
                                    for i in cpu.pronto:
                                        os.system('cls')
                                        print('Escolha a prioridade de cada processo:\n')
                                        print(f'  Prioridade do {i.nome}: ', end='')
                                        p = int(input(''))
                                        i.prioridade = p
                                case '2':
                                    print('Vamos continuar a corrida então...')
                                    sleep(3)
                                case _:
                                    print('Opção inválida, tente 1 ou 2\n')
                                    sleep(3)
                                    os.system('cls')
                                    continue
                            os.system('cls')
                            try:
                                p = next(g)
                            except StopIteration:
                                ordem = p[1]
                                break
                        print('FIM DA CORRIDA!!!')
                        sleep(3)
                        print('A ordem de chegada foi:')
                        lugar = 1
                        for i in ordem:
                            print(f'{lugar}º lugar - {i.nome}')
                            lugar += 1
                            sleep(1)
                        print('Foi uma ótima corrida, mas creio que teremos revanches *_*')
                        sleep(4)
                        print('Vamos realocar os processos.')
                        sleep(2)
                        p1 = Processo('sorteador', processo_1, 1)
                        p2 = Processo('movedor', processo_2, 2)
                        p3 = Processo('contador', processo_3, 3)
                        cpu.inserir(p1)
                        cpu.inserir(p2)
                        cpu.inserir(p3)
                        print('Aperte qualquer coisa para voltar para o menu:')
                        pausa = input('')
                        os.system('cls')
                    case _:
                        print('Opção inválida, tente 1 ou 2\n')
                        sleep(3)
                        os.system('cls')
                        continue
            case _:
                print('Opção inválida, tente 1 ou 2\n')
                sleep(3)
                os.system('cls')
                continue

if __name__ == '__main__':
    main()
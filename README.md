# Gerenciador-de-Processos

## 🏁 Simulador de Escalonamento de Processos
Bem-vindo(a) ao repositório do Simulador de Escalonamento de Processos, desenvolvido para a disciplina de Sistemas Operacionais do professor Fábio. Aqui, nossos três competidores internos (o Sorteador, o Movedor e o Contador) disputam corridas sob diferentes algoritmos de escalonamento. 🚀

**Observação importante: A única utilização de IA neste projeto foi a escrita criativa deste README.**

## 🎯 Objetivo do Projeto
O objetivo principal é apresentar, de forma lúdica e interativa, como funcionam algoritmos de escalonamento em sistemas operacionais. Para isso, criamos um “gran prix” de processos:

  Sorteador (processo_1): Gera números aleatórios e imprime resultados a cada iteração.

  Movedor (processo_2): Mantém uma lista de inteiros e “move” valores, exibindo cada movimento.

  Contador (processo_3): Incrementa ou decrementa um contador “maluco” e mostra seu andamento.

Esses três processos correm em duas modalidades de escalonamento com preempção:

  Round-Robin (tempo fixo para cada processo)

  Escalonamento por Prioridade (quem tiver maior prioridade avança primeiro)

No fim, temos uma “corrida” que mostra a ordem de chegada dos processos.

## 📂 Estrutura do Repositório

.
<br>
├── Processador.py
<br>
├── Processo.py
<br>
├── processos.py
<br>
├── algoritmos_escalonamento.py
<br>
├── main.py
<br>
├── README.md
<br>
└── LICENSE (se aplicável)

### Processador.py
Classe que gerencia as filas de processos (novo, pronto, executando) e controla a execução unitária de cada processo via generators.

### Processo.py
Modelo genérico de um processo, que armazena nome, função correspondente (generator) e prioridade, além de controlar o índice de execução interno e tempo inicial de medição.

### processos.py
Contém as três funções geradoras (generators) que simulam cada “corrida”:

  processo_1 (Sorteador)

  processo_2 (Movedor)

  processo_3 (Contador)

Cada generator pausa a cada passo, preservando seu estado interno para “continuar de onde parou”.

### algoritmos_escalonamento.py
Implementa os dois algoritmos:

  escalonamento_prioridade: Executa processos baseando-se na prioridade (permite mudanças de prioridade em tempo de execução).

  round_robin: Executa processos em fatias de tempo (quantum), realizando “trocas” até todos terminarem.

### main.py
Script interativo que inicializa o Processador, cria instâncias de Processo (com as funções do processos.py), exibe menus de escolha de algoritmo e conduz a “corrida” no terminal. Inclui animações de “Loading” e narrativas divertidas para envolver o usuário.

## 🚦 Sobre os Algoritmos
### 1. Round-Robin 🕐
Cada processo recebe um tempo fixo (quantum) para “rodar”.

Quando o quantum termina, surge um “TROCO” e o próximo processo da fila é executado.

Assim que um processo termina (gera StopIteration no generator), ele deixa a corrida.

A coleta de finalização forma a ordem de chegada.

### 2. Escalonamento por Prioridade ⭐
Cada processo possui um atributo .prioridade (inteiro maior = mais importante).

Em cada passo, o simulador escolhe o processo de maior prioridade para executar UMA iteração.

Você pode mudar as prioridades ao longo da corrida para atrapalhar ou favorecer competidores!

Ao atingir um ponto crítico (índice 90 num dos processos), é possível receber um “palpite” de quem está prestes a vencer e “jogar alto” mudando prioridades.

O vencedor é anunciado assim que todos os outros terminarem.

## 🚀 Considerações Finais
Esperamos que este simulador ajude você a compreender, de forma interativa, como funcionam algoritmos de escalonamento em sistemas operacionais. A “corrida” entre o Sorteador, o Movedor e o Contador mostra na prática:

Como a granularidade (yield unitário) permite preempção cooperativa.

Como diferentes prioridades mudam o desenrolar da execução.

Como o Round-Robin garante “fairness” e pode surpreender no resultado.

Divirta-se, aprenda e não hesite em propor melhorias, novos algoritmos ou extensões! 🏎️✨

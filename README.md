# Gerenciador-de-Processos

🏁 Simulador de Escalonamento de Processos
Bem-vindo(a) ao repositório do Simulador de Escalonamento de Processos, desenvolvido para a disciplina de Sistemas Operacionais do professor Fábio. Aqui, nossos três competidores internos (o Sorteador, o Movedor e o Contador) disputam corridas sob diferentes algoritmos de escalonamento. 🚀

Observação importante: A única utilização de IA neste projeto foi a escrita criativa deste README. Todo o código dos simuladores foi produzido manualmente pela equipe.

🎯 Objetivo do Projeto
O objetivo principal é apresentar, de forma lúdica e interativa, como funcionam algoritmos de escalonamento em sistemas operacionais. Para isso, criamos um “gran prix” de processos:

Sorteador (processo_1): Gera números aleatórios e imprime resultados a cada iteração.

Movedor (processo_2): Mantém uma lista de inteiros e “move” valores, exibindo cada movimento.

Contador (processo_3): Incrementa ou decrementa um contador “maluco” e mostra seu andamento.

Esses três processos correm em duas modalidades de escalonamento:

Round-Robin (tempo fixo para cada processo)

Escalonamento por Prioridade (quem tiver maior prioridade avança primeiro)

No fim, temos uma “corrida” que mostra a ordem de chegada dos processos.

📂 Estrutura do Repositório
css
Copiar
Editar
.
├── Processador.py
├── Processo.py
├── processos.py
├── algoritmos_escalonamento.py
├── main.py
├── README.md
└── LICENSE (se aplicável)
Processador.py
Classe que gerencia as filas de processos (novo, pronto, executando) e controla a execução unitária de cada processo via generators.

Processo.py
Modelo genérico de um processo, que armazena nome, função correspondente (generator) e prioridade, além de controlar o índice de execução interno e tempo inicial de medição.

processos.py
Contém as três funções geradoras (generators) que simulam cada “corrida”:

processo_1 (Sorteador)

processo_2 (Movedor)

processo_3 (Contador)

Cada generator pausa a cada passo, preservando seu estado interno para “continuar de onde parou”.

algoritmos_escalonamento.py
Implementa os dois algoritmos:

escalonamento_prioridade: Executa processos baseando-se na prioridade (permite mudanças de prioridade em tempo de execução).

round_robin: Executa processos em fatias de tempo (quantum), realizando “trocas” até todos terminarem.

main.py
Script interativo que inicializa o Processador, cria instâncias de Processo (com as funções do processos.py), exibe menus de escolha de algoritmo e conduz a “corrida” no terminal. Inclui animações de “Loading” e narrativas divertidas para envolver o usuário.

⚙️ Como Executar
Clone este repositório no seu computador:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Certifique-se de que você tem Python 3.8+ instalado (recomendado).

Instale dependências (se houver)
Não há bibliotecas externas obrigatórias além da stdlib do Python. Basta ter random, time, threading (já inclusos).

Execute o script principal:

bash
Copiar
Editar
python main.py
Você verá:

Mensagens de boas-vindas e “Loading” animados 🔄

Menu para consultar tempo de cada processo

Opção de corrida entre processos com escolha de algoritmo

Interaja com as opções na tela:

Ao escolher [1], cada processo será executado individualmente para medir seu tempo total.

Ao escolher [2], você participará da “corrida insana”:

Escolha entre Round-Robin ou Escalonamento por Prioridade.

Se Round-Robin, defina o quantum (1s, 0.5s ou 0.1s).

Se Prioridade, você mesmo ajusta as prioridades antes de iniciar.

O simulador exibirá em tempo real quem está em execução e, ao final, mostrará a ordem de chegada 🏆.

🚦 Sobre os Algoritmos
1. Round-Robin 🕐
Cada processo recebe um tempo fixo (quantum) para “rodar”.

Quando o quantum termina, surge um “TROCO” e o próximo processo da fila é executado.

Assim que um processo termina (gera StopIteration no generator), ele deixa a corrida.

A coleta de finalização forma a ordem de chegada.

2. Escalonamento por Prioridade ⭐
Cada processo possui um atributo .prioridade (inteiro maior = mais importante).

Em cada passo, o simulador escolhe o processo de maior prioridade para executar UMA iteração.

Você pode mudar as prioridades ao longo da corrida para atrapalhar ou favorecer competidores!

Ao atingir um ponto crítico (índice 90 num dos processos), é possível receber um “palpite” de quem está prestes a vencer e “jogar alto” mudando prioridades.

O vencedor é anunciado assim que todos os outros terminarem.

🎉 Demonstração de Uso
Tempo Individual:

Selecione “[1] Ver o tempo de cada processo individualmente”.

O programa aloca e dispara cada processo (“Sorteador”, “Movedor”, “Contador”) sequencialmente, mostrando quanto tempo cada um demora no seu loop completo.

Corrida Insana:

Selecione “[2] Corrida entre os processos!”.

Uma animação de “Loading...” prepara o ambiente.

A narração apresenta os competidores (com emojis e efeitos sonoros imaginários 🤩).

Você escolhe:

[1] Round-Robin

Define o quantum (1s, 0.5s ou 0.1s)

Pressiona uma tecla para “Em suas marcas... Já!”

A cada quantum, há um print de qual processo está em execução.

Ao final, o simulador exibe “1º lugar, 2º lugar, 3º lugar” com pausa dramática.

[2] Escalonamento por Prioridade

Escolhe novas prioridades para cada processo (você mesmo dita números).

Pressiona uma tecla para “COMEÇAR A CORRIDA”.

O simulador chama escalonamento_prioridade como generator:

Imprime mensagens sobre quem está em execução (de acordo com prioridade).

Ao chegar a um índice quase vencedor (i = 90), o generator devolve um palpite de qual processo lidera, e o programa pergunta se você quer mudar prioridades antes de continuar.

Ao fim, exibe a ordem de chegada e sugere “revanches” futuramente.

🔧 Detalhes de Implementação
Generators (Yields)
Cada função em processos.py (processo_1, processo_2, processo_3) foi adaptada para funcionar como um generator. Em vez de rodar todo o laço de uma vez, elas:

Recebem index (ponto de reinício) e tempo (timestamp inicial).

Executam apenas uma iteração do loop a cada chamada de next(gen).

Chamam yield ao final de cada iteração, “pausando” o generator e guardando estado (índice atual, contadores, listas).

Ao terminar todas as iterações (i >= num), imprimem o tempo total e retornam, causando StopIteration.

Classe Processo (Processo.py)
Abstrai um “processo” genérico, armazenando:

nome (string)

funcao (generator factory)

prioridade (int)

indice (onde parou, para chamar generator a partir do ponto correto)

tempo_inicial (timestamp para medir duração real)

Seu método executar() retorna o generator a partir de indice e registra tempo_inicial na primeira vez.

Classe Processador (Processador.py)
Gerencia as listas internas:

novo (não utilizada ativamente neste projeto, mas mantida para possíveis extensões)

pronto (fila de processos aguardando execução)

executando (processo atual em execução)

O método inserir() adiciona processos a pronto. O método executar(processo):

Se não há executando, define o escolhido como executando e o remove de pronto.

Se já há um executando, devolve-o a pronto, seta o novo como atual e remove-o de pronto.

Imprime quem está executando, “sleep(0.05)” para simular tempo mínimo, e pede ao processo para rodar UMA unidade (self.executando.executar() → retorna o generator).

Tenta fazer next(generator) para obter novo indice; se StopIteration ocorre, imprime que o processo terminou e aguarda 5s antes de liberar CPU.

Algoritmos de Escalonamento (algoritmos_escalonamento.py)

escalonamento_prioridade(cpu) (generator ):

Enquanto há pronto ou alguém executando, escolhe o de maior prioridade em pronto, chama cpu.executar(...).

Se o índice de algum processo atingir 90 (ponto “quase vencedor”), devolve via yield [processo, chegada_list] para possibilitar mudança de prioridade.

A cada passo, atualiza quem está executando e, ao terminar, registra ordem de chegada.

round_robin(cpu, quantu):

Enquanto há processos em pronto ou alguém executando, pega o primeiro de pronto, chama cpu.executar(p) repetidamente até quantum expirar ou processo terminar.

Se processo terminar, registra chegada; caso contrário, faz “TROCO” e passa adiante.

Devolve a lista de chegadas na ordem final.

Script Principal (main.py)

Instancia Processador e três Processo('sorteador', processo_1, prio), etc.

Exibe menus com narrativas divertidas (incluindo emojis, “Loading...” animado e pausas dramáticas).

Permite explorar os tempos individuais ou a “corrida” completa, interagindo e realocando processos conforme escolha do usuário.

🤝 Créditos & Agradecimentos
Professor Fábio: Orientador e avaliador deste trabalho de Sistemas Operacionais.

Equipe de Desenvolvimento: Alunos responsáveis pela implementação manual dos simuladores e adaptação das funções para generators.

IA (ChatGPT): Utilizada apenas para a escrita criativa deste README (uso mínimo e pontual 😜).

📜 Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

🚀 Considerações Finais
Esperamos que este simulador ajude você a compreender, de forma interativa, como funcionam algoritmos de escalonamento em sistemas operacionais. A “corrida” entre o Sorteador, o Movedor e o Contador mostra na prática:

Como a granularidade (yield unitário) permite preempção cooperativa.

Como diferentes prioridades mudam o desenrolar da execução.

Como o Round-Robin garante “fairness” e pode surpreender no resultado.

Divirta-se, aprenda e não hesite em propor melhorias, novos algoritmos ou extensões! 🏎️✨

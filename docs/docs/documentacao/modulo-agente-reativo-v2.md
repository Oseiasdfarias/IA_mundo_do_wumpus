---
sidebar_position: 3
custom_edit_url: null
---

# Módulo agente-reativo-v2

## Descrição do módulo

O **módulo agente-reativo-v2** implementa a **Classe AgenteReativoV2** essa classe é uma melhoria da **Classe AgenteReativoV1**  do **módulo agente-reativo-v2**.

## Expeficicações do Agente Reativo (V2)

- Esta versão engloba a versão 1 e, mais, aos moldes do “Modelo Linear de Estruturas de Agentes”;
- Estrutura de memória, que pode ser: uma lista; uma matriz - réplica do ambiente, com anotações feitas pelo agente; ou, outra estrutura de dados definida como mais adequada pela equipe;
- Mecanismo mais inteligente para escolha da regra a ser aplicada, em caso de duas ou mais possíveis de serem utilizadas em determinado instante. Na primeira versão foi utilizada a Estratégia Aleatória. Logo, há liberdade para definir a melhor estratégia para essa finalidade;
- Além disso, uso do conhecimento registrado na memória para auxiliar o processo de escolha da regra a ser aplicada (Inferência? Planejamento?);
- Além disso, uso do conhecimento registrado na memória para auxiliar o processo de escolha da regra a ser aplicada (Inferência? Planejamento?);
- E o que mais a equipe deseje projetar: “- Usem as vossas criatividades”
- Ao final, após o projeto deste Agente, pede-se que este seja classificado de acordo com as estruturas de agentes e justificada a classificação.


## Classe

### `class AgenteReativoV1:`

#### Parâmetros da classe

| Parâmetros           | Descrição |
|        :---          |    :----   |
| `ambiente: Ambiente`    | Esse parâmetro recebe uma instáncia da classe Ambiente.  |

#### Métodos da classe

| Métodos              | Descrição |
|          :---        |    :----   |
| `AgenteReativoV2.opcoes_mov_agente`    |Verifica as possíveis opções de movimentação do agente para a posição atual.  |
| `AgenteReativoV2.__opcoes_mov_agente`    | Verifica as possíveis opções de movimentação do agente para a posição atual. |
| `AgenteReativoV2.verificar_morte_agente_wumpus`    | Verifica se o agente foi morto pelo Wumpus. |
| `AgenteReativoV2.verificar_morte_agente_poco`    | Verifica se o agente caiu no poço. |
| `AgenteReativoV2.pegar_outro`    | Pega o ouro caso esteja na mesma posição do agente. |
| `AgenteReativoV2.status_agente_ouro`    | Informa se o agente pegou ou não o ouro. |
| `AgenteReativoV2.__sentir_fedor`    | Verifica se na posição atual do agente existe a percepção de fedor. |
| `AgenteReativoV2.sortear_pos`    | Sortea um item de uma lista, método usado para sortear posições |
| `AgenteReativoV2.verificar_atirar_wumpus`    | Verifica se existe fedor na posição atual usando o método `AgenteReativoV2.__sentir_fedor`, a partir dessa validação, atira em uma direção para tentar matar o wumpus. |
| `AgenteReativoV2.verificar_vitorio`    | Verifica se o agente venceu o jogo. |
| `AgenteReativoV2.ganhou_jogo`    | Imprime a informação se o agente ganhou ou perdeu a partida. |
| `AgenteReativoV2.get_opcoes_mov_agente`    | retorna as posições possíveis para o agente se mover, levando em consideração a posição atual. |
| `AgenteReativoV1.mostrar_opcoes_mov`    |  Imprime as possições posiveis de o agente se mover, levando em consideração a posição atual|




Para que seja possível usar a classe `AgenteReativoV2` é preciso instáncia um objeto `Ambiente` e passar como argumento para a Classe `AgenteReativoV2`, o Exemplo 1 mostra a estrutura.

## Exemplos `1`

### Tamanho do mundo `3x3`

**Código:**
```python title="main.py"
from ia_wumpus import AgenteReativoV1
from ia_wumpus import Ambiente

amb = Ambiente(dimensao_ambiente=3)
agente = AgenteReativoV1(amb)
agente.verificar_atirar_wumpus()

amb.mostrar_ambiente()
pos_mov = agente.sortear_pos(agente.get_opcoes_mov())
amb.atualiza_pos_agente(pos_mov)
amb.mostrar_ambiente()
```

**Saída:**

```
====== Menu - Mundo do Wumpus ======
        + 1 - Wumpus
        + 2 - Poços
        + 3 - Ouro
        + 4 - Agente
====================================
Agente sentiu fedor
Pos tiro (0, 1)
Errou o tiro!

Mundo do Wumpus:
[[4 0 0]
 [1 2 0]
 [3 2 2]]

Mundo do Wumpus:
[[0 4 0]
 [1 2 0]
 [3 2 2]]
```


## Exemplos `2`

Para fazer o jogo execultar até obter uma vitória, podemos usar loops while aninhados, dessa forma o primeiro loop só terminal quando o ouver uma vitóia, e o segundo loop é responsável por realizar a dinámica do ambiente.

### Tamanho do mundo `5x5`

**Código:**
```python title="main.py"
from ia_wumpus import Ambiente
from ia_wumpus import AgenteReativoV1
import os

rodadas = 0
passos = 0

while True:
    passos = 0
    amb = Ambiente(dimensao_ambiente=5, t_pausa=0.0)
    amb.mostrar_ambiente()
    agente = AgenteReativoV1(amb)
    p = agente.printw
    while True:
        agente.verificar_atirar_wumpus()
        pos_mov = agente.sortear_pos(agente.get_opcoes_mov())
        amb.atualiza_pos_agente(pos_mov)
        amb.mostrar_ambiente()
        agente.pegar_outro()
        agente.status_agente_ouro()
        agente.verificar_morte_agente_wumpus()
        agente.verificar_morte_agente_poco()
        if agente.verificar_vitorio():
            passos += 1
            rodadas += 1
            agente.ganhou_jogo()
            p(f"Qt. de passos no Ambiente: {passos}")
            p(f"Qt. de rodadas: {rodadas}\n")
            os._exit(0)
        elif agente.morreu:
            break
        passos += 1
    p(f"Qt. de passos no Ambiente: {passos}")
    rodadas += 1

```


**Saída:**

Dependendo da quantidade de vezes que o agente morre, a saída pode ser extensa, abaixo é mostrado
as últimas saídas para uma execução do código.

```
.
.
.

Mundo do Wumpus:
[[0 4 0 0 2]
 [0 0 0 0 2]
 [0 0 0 0 0]
 [2 0 0 0 2]
 [0 1 0 0 2]]
[INFO:] O agente está com o ouro!

Mundo do Wumpus:
[[4 0 0 0 2]
 [0 0 0 0 2]
 [0 0 0 0 0]
 [2 0 0 0 2]
 [0 1 0 0 2]]
[INFO:] O agente está com o ouro!

============== Fim de Jogo ==============
          VITÓRIA DO AGENTE
=========================================

Qt. de passos no Ambiente: 8
Qt. de rodadas: 6

```

Para que o `agente` vença a partida, ele deve pega o ouro e voltar para a posição inicial `(0, 0)`. Nessa execução precisou de 12 partidas para que o agente vencesse o jogo.
---
sidebar_position: 2
custom_edit_url: null
---

# Módulo agente-reativo-v1

## Descrição do módulo

O **módulo agente-reativo-v1** implementa a **Classe AgenteReativoV1** que é responsável por criar a dinâmica do agente no **Mundo de Wunpus**, possibilitando que o agente se mova no ambiente e tome as decisões necessárias para cumprir a tarefa, que no caso desse agente é pegar o ouro e retornar a posição inicial, para isso, é preciso não cair em poços ou ter contato com o wumpus, caso isso ocorra o agente morre.

## Expeficicações do Agente Reativo (V1)

- O comportamento do Agente é definido a partir de seu conjunto de regras:
    + Se < percepções > então < ação >.
- Este conjunto de regras (ou Base de Conhecimento) deve ser especificado por meio de uma tabela, aos moldes da que foi especificada, inicialmente, na “Aula 04';
- A partir da especificação, o próximo passo é codificar o Agente e integrar ao “Gerador Aleatório de Ambientes, de forma a ossibilitar a realização de testes de validação para posterior avaliação de performance;
- Obs.: Serão projetadas várias versões deste Agente. Nesta primeira versão, ele utiliza apenas o conjunto de regras como base de conhecimento. Ou seja, não tem memória e nenhum outro mecanismo mais sofisticado para escolher qual das possíveis regras utilizar. Para isto, deve ser uma escolha aleatória. Além disso, ele tem apenas uma única flecha.


## Classe

### `class AgenteReativoV1:`

#### Parâmetros da classe

| Parâmetros           | Descrição |
|        :---          |    :----   |
| `ambiente: Ambiente`    | Esse parâmetro recebe uma instáncia da classe Ambiente.  |

#### Métodos da classe

| Métodos              | Descrição |
|          :---        |    :----   |
| `AgenteReativoV1.opcoes_mov_agente`    |Verifica as possíveis opções de movimentação do agente para a posição atual.  |
| `AgenteReativoV1.__opcoes_mov_agente`    | Verifica as possíveis opções de movimentação do agente para a posição atual. |
| `AgenteReativoV1.verificar_morte_agente_wumpus`    | Verifica se o agente foi morto pelo Wumpus. |
| `AgenteReativoV1.verificar_morte_agente_poco`    | Verifica se o agente caiu no poço. |
| `AgenteReativoV1.pegar_outro`    | Pega o ouro caso esteja na mesma posição do agente. |
| `AgenteReativoV1.status_agente_ouro`    | Informa se o agente pegou ou não o ouro. |
| `AgenteReativoV1.__sentir_fedor`    | Verifica se na posição atual do agente existe a percepção de fedor. |
| `AgenteReativoV1.sortear_pos`    | Sortea um item de uma lista, método usado para sortear posições |
| `AgenteReativoV1.verificar_atirar_wumpus`    | Verifica se existe fedor na posição atual usando o método `AgenteReativoV1.__sentir_fedor`, a partir dessa validação, atira em uma direção para tentar matar o wumpus. |
| `AgenteReativoV1.verificar_vitorio`    | Verifica se o agente venceu o jogo. |
| `AgenteReativoV1.ganhou_jogo`    | Imprime a informação se o agente ganhou ou perdeu a partida. |
| `AgenteReativoV1.get_opcoes_mov_agente`    | retorna as posições possíveis para o agente se mover, levando em consideração a posição atual. |
| `AgenteReativoV1.mostrar_opcoes_mov`    |  Imprime as possições posiveis de o agente se mover, levando em consideração a posição atual|




<!--

### Métodos

### `Ambiente.__add_pos_obj()`

Posiciona o objeto em um local válido no ambiente, para isso, usa o método `Ambiente.__sortear_pos` para sortear a posição.

### `Ambiente.__sortear_pos()`

Sorteia uma posição para adicionar um objeto.

### `Ambiente.__add_percepcoes_obj(objeto, pos)`

Posiciona as percepções de um dado objeto ao seu redor.

### `Ambiente.__add_pos_wumpus()`

Posiciona o(s) Wumpos e as suas percepções no ambiente, usa os métodos `Ambiente.__add_pos_obj` e `Ambiente.__add_percepcoes_obj` para realizar a lógica.

### `Ambiente.__add_pos_pocos()`

Posiciona os poços e as suas percepções no ambiente, usa os métodos `Ambiente.add_pos_obj` e  `Ambiente.__add_percepcoes_obj`  para realizar a lógica.

### `Ambiente.__add_pos_ouro()`

Posiciona o(s) Ouro(s) e as suas percepções no ambiente, usa o método `Ambiente.__add_pos_obj` para realizar a lógica.

### `Ambiente.__add_pos_agente()`

Adiciona o Agente na posição `[0, 0]`

### `Ambiente.__menu()`

Menu com as descrições dos objetos.

### `Ambiente.infos_ambiente()`

Mostra informações sobre o Mundo do Wumpus.

### `Ambiente.mostrar_ambiente()`

Mostra a matriz que representa o Mundo do Wumpus.

### `Ambiente.mostrar_percepcoes()`

 Mostra as posições das percepções dos objetos.
 
 -->

Para que seja possível usar a classe `AgenteReativoV1` é preciso instáncia um objeto `Ambiente` e passar como argumento para a Classe `AgenteReativoV1`, o Exemplo 1 mostra a estrutura.

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
from rich import print
import os

rodadas = 0
passos = 0

while True:
    passos = 0
    amb = Ambiente(dimensao_ambiente=5, t_pausa=0.0)
    amb.mostrar_ambiente()
    agente = AgenteReativoV1(amb)
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
            print(f"[red italic bold]Qt. de passos no Ambiente: {passos}[/]")
            print(f"[red italic bold]Qt. de rodadas: {rodadas}\n[/]")
            os._exit(0)
        elif agente.morreu:
            break
        passos += 1
    print(f"[red italic bold]Qt. de passos no Ambiente: {passos}[/]")
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
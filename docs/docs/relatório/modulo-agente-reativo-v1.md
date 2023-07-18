---
sidebar_position: 3
custom_edit_url: null
---

# Módulo agente-reativo-v1

## Descrição do Agente Reativo (V1)

O **Agente Reatico V1** tem como principal característica não possuir memória, dessa forma, suas ações são baseadas no estado atual, para o implementação desse agente foi usada uma classe que interage com a classe do ambiente, assim é possivel a partir das percepções da possição atual obter o próximo passo, para realizar essa ação como o agente reativo v1 não possui memória, pegamos as possiveis posoções que o agente pode se mover e sorteamos aleatoriamente uma delas.


## Expeficicações do Agente Reativo (V1)

- O comportamento do Agente é definido a partir de seu conjunto de regras:
    + Se < percepções > então < ação >.
- Este conjunto de regras (ou Base de Conhecimento) deve ser especificado por meio de uma tabela, aos moldes da que foi especificada, inicialmente, na “Aula 04';
- A partir da especificação, o próximo passo é codificar o Agente e integrar ao “Gerador Aleatório de Ambientes, de forma a ossibilitar a realização de testes de validação para posterior avaliação de performance;
- Obs.: Serão projetadas várias versões deste Agente. Nesta primeira versão, ele utiliza apenas o conjunto de regras como base de conhecimento. Ou seja, não tem memória e nenhum outro mecanismo mais sofisticado para escolher qual das possíveis regras utilizar. Para isto, deve ser uma escolha aleatória. Além disso, ele tem apenas uma única flecha.


### Exemplo


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
---
sidebar_position: 2
custom_edit_url: null
---

# Ambiente do Mundo do Wumpus

## Descrição do módulo

O Mundo de Wumpus é um jogo antigo de computador que representa um ambiente artificial desafiador para testar o raciocínio lógico de agentes inteligentes. O objetivo é explorar uma caverna composta por compartimentos interconectados, com o desafio de encontrar ouro enquanto evita o Wumpus, um monstro mortal, e abismos perigosos. O agente começa no compartimento `[0, 0]` e pode eliminar o Wumpus com uma única flecha, tornando a busca pelo ouro ainda mais tensa. A tarefa é encontrar o tesouro e retornar ao ponto inicial para escapar da caverna. Uma jornada emocionante que exige habilidade estratégica e astúcia do agente.


## Tabela Verdade

| | | | | | | | | | | | | | | |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| | | | | | | | | | | | | | | |
| |Percepções| | | | |Ações| | | | | | | | |
| |Local|Brisa|Grito|Fedor|Brilho|Movimentar| | | |Atirar| | | |Pegar|
| | | | | | |N|S|L|O|N|S|L|O| |
| |(0, 0)|-|-|-|-|-|-|x|-|-|-|-|-|-|
| |(0, 0)|-|-|-|-|-|x|-|-|-|-|-|-|-|
| |(0, 0)|x|-|-|-|-|-|x|-|-|-|-|-|-|
| |(0, 0)|x|-|-|-|-|x|-|-|-|-|-|-|-|
| |(0, 0)|-|-|x|-|-|-|x|-|-|-|-|-|-|
| |(0, 0)|-|-|x|-|-|x|-|-|-|-|-|-|-|
| |(0, 0)|-|-|x|-|-|-|-|-|-|-|x|-|-|
| |(0, 0)|-|-|x|-|-|-|-|-|-|x|-|-|-|
| |(0, 0)|-|x|x|-|-|-|x|-|-|-|-|-|-|
| |(0, 0)|-|x|x|-|-|x|-|-|-|-|-|-|-|
| |(0, 0)|x|-|x|-|-|-|-|-|-|-|x|-|-|
| |(0, 0)|x|-|x|-|-|-|-|-|-|x|-|-|-|
| |(0, 0)|x|-|x|-|-|-|x|-|-|-|-|-|-|
| |(0, 0)|x|-|x|-|-|x|-|-|-|-|-|-|-|
| |(0 > x > n-2, 0)|-|-|-|-|-|x|-|-|-|-|-|-|-|
| |(0 > x > n-2, 0)|-|-|-|-|-|-|x|-|-|-|-|-|-|
| |(0 > x > n-2, 0)|-|-|-|-|-|-|-|x|-|-|-|-|-|
| |(0 > x > n-2, 0)|x|-|-|-|-|x|-|-|-|-|-|-|-|
| |(0 > x > n-2, 0)|x| |-|-|-|-|x|-|-|-|-|-|-|
| |(0 > x > n-2, 0)|x|-|-|-|-|-|-|x|-|-|-|-|-|
| |(0 > x > n-2, 0)|-|-|x|-|-|x|-|-|-|-|-|-|-|
| |(0 > x > n-2, 0)|-|-|x|-|-|-|x|-|-|-|-|-|-|
| |(0 > x > n-2, 0)|-|-|x|-|-|-|-|x|-|-|-|-|-|
| |(0 > x > n-2, 0)|-|-|x|-|-|-|-|-|-|x|-|-|-|
| |(0 > x > n-2, 0)|-|-|x|-|-|-|-|-|-|-|x|-|-|
| |(0 > x > n-2, 0)|-|-|x|-|-|-|-|-|-|-|-|x|-|
| |(0 > x > n-2, 0)|-|x|-|-|-|-|-|-|-|-|-|-|x|
| |(0 > x > n-2, 0)|x|-|x|-|-|x|-|-|-|-|-|-|-|
| |(0 > x > n-2, 0)|x|-|x|-|-|-|x|-|-|-|-|-|-|
| |(0 > x > n-2, 0)|x|-|x|-|-|-|-|x|-|-|-|-|-|
| |(0 > x > n-2, 0)|x|-|x|-|-|-|-|-|-|x|-|-|-|
| |(0 > x > n-2, 0)|x|-|x|-|-|-|-|-|-|-|x|-|-|
| |(0 > x > n-2, 0)|x|-|x|-|-|-|-|-|-|-|-|x|-|
| |(0 > x > n-2, 0)|x|-|x|-|-|-|-|-|-|-|-|-|-|


## Exemplos `1`

### Tamanho do mundo `3x3`

**Código:**
```python title="main.py"
from ia_wumpus import Ambiente

amb = Ambiente(dimensao_ambiente=3)
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

Mundo do Wumpus:
[[4 1 0]
 [2 2 3]
 [0 0 2]]
```

## Exemplos `2`

Esse exemplo mostra a matriz que representa o ambiente com os objetos em suas posições e as posições
das percepções dos objetos.

### Tamanho do mundo `3x3`

**Código:**
```python title="main.py"
from ia_wumpus import Ambiente


amb = Ambiente(dimensao_ambiente=3)
amb.mostrar_ambiente()
amb.mostrar_percepcoes()
```

**Saída:**

```
====== Menu - Mundo do Wumpus ======
        + 1 - Wumpus
        + 2 - Poços
        + 3 - Ouro
        + 4 - Agente
====================================

Mundo do Wumpus:
[[4 0 0]
 [2 1 3]
 [2 0 2]]

======== Posições das Percepções - Mundo do Wumpus ========
Posição Fedor  :
        [(1, 2), (1, 0), (2, 1), (0, 1)]
Posições Brisa :
        [(0, 1), (1, 2), (2, 1), (1, 2), (0, 2), (0, 0), (1, 1)]
Posição Brilho :
        [(2, 1)]
============================================================
```

## Exemplos `3`

Para realizar a atualização basta usar o método `Ambiente.mostrar_ambiente()` passando uma tupla
com as coordenadas válidas dos eixos `x` e `y`, Para visualizar a atualização da posição, basta usar o 
método `Ambiente.mostrar_ambiente()` após atualizar a posição.

### Tamanho do mundo `3x3`

**Código:**
```python title="main.py"
from ia_wumpus import Ambiente


amb = Ambiente(dimensao_ambiente=3)
amb.mostrar_ambiente()
amb.atualiza_pos_agente((1, 1))
amb.mostrar_ambiente()
amb.atualiza_pos_agente((2, 2))
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

Mundo do Wumpus:
[[4 3 0]
 [0 2 2]
 [1 0 2]]

Mundo do Wumpus:
[[0 3 0]
 [0 4 2]
 [1 0 2]]

Mundo do Wumpus:
[[0 3 0]
 [0 0 2]
 [1 0 4]]
```

O exemplo 3 mostra a atualização do Agente, para cada chamada do método `Ambiente.mostrar_ambiente()`
o Agente anda uma casa na diagonal.
---
sidebar_position: 1
custom_edit_url: null
---

# Módulo ambiente

O **módulo ambiente** implementa a **Classe Ambiente** que é responsável por construir o cenário do **mundo do Wumpus**, além disso, a classe implementa métodos que posicionam os objetos e suas **percepções** de forma correta no ambiente.

## Classe

### `class Ambiente:`

#### Parâmetros da classe

| Parâmetros           | Descrição |
|        :---          |    :----   |
| `dimensao_ambiente`    | Esse parâmetro define o tamanho do Mundo do Wumpos, o ambiente é sempre uma matriz quadrada.  |
| `wumpus`               | Define a quantidade de Wumpus no Ambiente. |
| `ouro`                 | Define a quantidade de Ouro no Ambiente  |

#### Métodos da classe

| Métodos              | Descrição |
|          :---        |    :----   |
| `Ambiente.atualiza_pos_agente`    |Atualiza a posição do Agente no Ambiente.  |
| `Ambiente.get_pos_objetos`    |Obtem as posições dos Objetos no Ambiente. |
| `Ambiente.get_percepcoes`    |Obtem as percepções dos Objetos no Ambiente. |
| `Ambiente.__add_pos_obj_map`        | Posiciona o objeto em um local válido no ambiente, para isso, usa o método `Ambiente.__sortear_pos` para sortear a posição.  |
| `Ambiente.__salvar_pos_objetos`        | PArmazena as posições dos Objetos em um dicionário Python.  |
| `Ambiente.__sortear_pos`        | Sorteia uma posição para adicionar um objeto.  |
| `Ambiente.__add_percepcoes_obj` | Posiciona as percepções de um dado objeto ao seu redor. |
| `Ambiente.__add_pos_wumpus`     | Posiciona o(s) Wumpos e as suas percepções no ambiente, usa os métodos `Ambiente.__add_pos_obj_map` e `Ambiente.__add_percepcoes_obj` para realizar a lógica.  |
| `Ambiente.add_pos_pocos`      | Posiciona os poços e as suas percepções no ambiente, usa os métodos `Ambiente.__add_pos_obj_map` e  `Ambiente.__add_percepcoes_obj`  para realizar a lógica.  |
| `Ambiente.__add_pos_ouro`       | Posiciona o(s) Ouro(s) e as suas percepções no ambiente, usa o método `Ambiente.__add_pos_obj_map` para realizar a lógica. |
| `Ambiente.__add_pos_agente`     | Adiciona o Agente na posição `[0, 0]`  |
| `Ambiente.__menu`               | Menu com as descrições dos objetos.  |
| `Ambiente.infos_ambiente`     | Mostra informações sobre o Mundo do Wumpus.  |
| `Ambiente.mostrar_ambiente`   | Mostra a matriz que representa o Mundo do Wumpus.  |
| `Ambiente.mostrar_percepcoes`   | Mostra as posições das percepções dos objetos. |


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
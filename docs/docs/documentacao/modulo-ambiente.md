---
sidebar_position: 1
custom_edit_url: null
---

# Módulo ambiente

O **módulo ambiente** implementa a **Classe Ambiente** que é responsável por construir o cenário do **mundo do Wumpus**, além disso, a classe implementa métodos que posiciona as **percepções** dos objetos corretamente no ambiente.

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
| `Ambiente.__add_pos_obj`        | Posiciona o objeto em um local válido no ambiente, para isso, usa o método `Ambiente.sortear_pos` para sortear a posição.  |
| `Ambiente.__sortear_pos`        | Sorteia uma posição para adicionar um objeto.  |
| `Ambiente.__add_percepcoes_obj` | Posiciona as percepções de um dado objeto ao seu redor. |
| `Ambiente.__add_pos_wumpus`     | Posiciona o(s) Wumpos e as suas percepções no ambiente, usa os métodos `Ambiente.__add_pos_obj` e `Ambiente.__add_percepcoes_obj` para realizar a lógica.  |
| `Ambiente.add_pos_pocos`      | Posiciona os poços e as suas percepções no ambiente, usa os métodos `Ambiente.add_pos_obj` e  `Ambiente.__add_percepcoes_obj`  para realizar a lógica.  |
| `Ambiente.add_pos_ouro`       | Posiciona o(s) Ouro(s) e as suas percepções no ambiente, usa o método `Ambiente.add_pos_obj` para realizar a lógica. |
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

## Exemplos

### Mundo de tamanho `3x3`

**Código:**
```python
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
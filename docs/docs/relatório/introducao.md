---
sidebar_position: 1
custom_edit_url: null
---

# Relatório - Mundo do Wumpus

<h1> <center> Universidade Federal do Pará</center> </h1>
<h1> <center> Campus Universitário de Tucuruí</center> </h1>
<h1> <center> Faculdade de Engenharia Elétrica</center> </h1>
<h1> <center> Disciplina: Inteligência Computacional</center> </h1>


### Grupo 3

**Professor Dr:** Otávio Noura Teixeira

**Alunos:**
- Ângelo Neto Cruz Aragão - 201933940002
- Jonanes Martins Galvão  - 201933940007
- Oséias Dias de Farias   - 201733940002



# Introdução

O Mundo de Wumpus é um clássico jogo de computador, conhecido por ser um domínio artificial que estimula o raciocínio lógico. Apesar de sua simplicidade em comparação aos jogos modernos, o Mundo de Wumpus oferece um ambiente desafiador para testar a inteligência de agentes.

![Mundo do Wumpus](./img/mw.png)

O ambiente consiste em uma caverna, onde compartimentos estão interconectados por passagens. Em um desses compartimentos reside o temível Wumpus, um monstro que devora qualquer intruso que ouse entrar em seu domínio. Além disso, alguns compartimentos escondem abismos mortais, exceto para o Wumpus, já que é grande demais para cair neles. O único motivo para um agente se aventurar nesse ambiente hostil é a busca pelo ouro escondido.

O agente possui apenas uma chance de atirar uma flecha, podendo eliminar o Wumpus se tiver sorte e precisão. A partida começa sempre com o agente posicionado no compartimento [1,1]. A tarefa do agente é encontrar o ouro e, em seguida, retornar à posição [1,1] para conseguir escapar da caverna com segurança. É um verdadeiro teste de habilidade e estratégia para qualquer agente inteligente.

## Caracterização do mundo Wumpus:

- Parcialmente observável: conhece apenas as percepções locais
- Determinístico: o resultado é precisamente especificado
- Sequencial: nível subsequente de ações realizadas
- Estático: Wumpus, os poços estão imóveis
- Discreto: ambiente discreto
- Agente único: O agente baseado em conhecimento é o único agente, - - enquanto o wumpus é considerado o recurso do ambiente.


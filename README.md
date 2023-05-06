
<center>
    <img src="utils/logo.png" alt="Girl in a jacket" style="width:60px">
</center>

<center>

### Universidade Federal do Pará

### Campus Universitário de Tucuruí

### Faculdade de Engenharia Elétrica

</center>

<br>

# Mundo do Wumpus - Intelegência Computacional

Ambiente para estudo de modelos de Apredizagem de Máquina da disciplina de Inteligência Computacional.

<br>

## Versoões do Projeto

<br>

## [Link Versão 00](https://github.com/Oseiasdfarias/IA_mundo_do_wumpus/tree/versao_0)

**Etapa 1 - Gerador Aleatório de Ambientes do Mundo do Wumpus**

+ Tamanho (n) = ordem(n) da matriz quadrada (n > 3). Linha e coluna = (n - 1);

+ Objetos: poços (p), Wumpus (W) e ouro (o). Quantidade?
[São parâmetros definidos pelo usuário (p, W, o = O). *E, também, podem ser atribuídos automaticamente, de acordo com o tamanho do ambiente (n), via a definição de alguma regra]*.

+ A partir dos objetos, posicionar no ambiente, também, as percepções geradas por cada um
deles;

+ A casa (0,0) é a única que não pode ter nenhum objeto, pois é a posição inicial do Agente;

+ Onde houver poço não pode ser posicionado o ouro e o Wumpus. No entanto, estes podem
ser posicionados em quaisquer uma das outras casas.



<br>

<center>
    <img src="utils/code_demo.png" alt="Demostração do Anbiente de desenvolvimento." style="width:900px">
</center>
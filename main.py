from ia_wumpus import Ambiente
from ia_wumpus import AgenteReativoV1, AgenteReativoV2
# import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
from ia_wumpus import __version__
import os
from copy import deepcopy
from typing import List


ensaiosV1: List[List] = [[], []]
ensaiosV2: List[List] = [[], []]


amb_base = Ambiente(dimensao_ambiente=15, t_pausa=0.0)
backup_amb = deepcopy(amb_base)

cont = 0


def graficos(ensaiosV1, ensaiosV2):
    plt.subplot(2, 1, 1)
    plt.plot(ensaiosV1[0], label="Passos do Agente V1", color="b")
    plt.plot(ensaiosV2[0], linestyle='--',
             label="Passos do Agente V2", color="r")
    plt.xlabel("Ensaios")
    plt.ylabel("Rodadas")

    plt.subplot(2, 1, 2)
    plt.plot(ensaiosV1[1], label="Rodadas  V2", color="b")
    plt.plot(ensaiosV2[1], linestyle='--',
             label="Rodadas  V2", color="r")
    plt.xlabel("Ensaios")
    plt.ylabel("passos")

    plt.show()


def TesteV1():
    rodadas = 0
    global cont
    while True:
        passos = 0
        amb = deepcopy(backup_amb)
        amb.mostrar_ambiente()
        agente = AgenteReativoV1(amb)
        p = agente.printw
        while True:
            agente.verificar_atirar_wumpus()

            pos_mov = agente.sortear_pos(agente.get_opcoes_mov())

            amb.atualiza_pos_agente(pos_mov)
            agente.pegar_outro()
            agente.verificar_morte_agente_wumpus()
            # agente.verificar_morte_agente_poco()
            if agente.verificar_vitorio():
                # amb.mostrar_ambiente()
                passos += 1
                rodadas += 1
                ensaiosV1[0].append(passos)
                ensaiosV1[1].append(rodadas)
                agente.ganhou_jogo()
                p(f"Versão: [blink]{__version__}[/blink]")
                p(f"Qt. de passos no Ambiente: {passos}")
                p(f"Qt. de rodadas: {rodadas}\n")
                cont += 1
                rodadas = 0
                break
            elif agente.morreu:
                # rodadas += 1
                amb.mostrar_ambiente()
                break
            passos += 1
        rodadas += 1
        # p(f"Qt. de passos no Ambiente: {passos}")
        p(f"Qt. rodadas: {rodadas}")
        if cont > 50:
            break
            # os._exit(0)


cont1 = 0


def TesteV2():
    rodadas = 0
    global cont1
    while True:
        passos = 0
        amb = deepcopy(backup_amb)
        amb.mostrar_ambiente()
        agente = AgenteReativoV2(amb)
        p = agente.printw
        while True:
            agente.verificar_atirar_wumpus()

            # pos_mov = agente.sortear_pos(agente.get_opcoes_mov())
            pos_mov = agente.verificar_pos_segura()
            amb.atualiza_pos_agente(pos_mov)
            agente.pegar_outro()
            agente.verificar_morte_agente_wumpus()
            # agente.verificar_morte_agente_poco()
            if agente.verificar_vitorio():
                # amb.mostrar_ambiente()
                passos += 1
                rodadas += 1
                ensaiosV2[0].append(passos)
                ensaiosV2[1].append(rodadas)
                agente.ganhou_jogo()
                p(f"Versão: [blink]{__version__}[/blink]")
                p(f"Qt. de passos no Ambiente: {passos}")
                p(f"Qt. de rodadas: {rodadas}\n")
                cont1 += 1
                rodadas = 0
                break
            elif agente.morreu:
                # rodadas += 1
                amb.mostrar_ambiente()
                break
            passos += 1
        rodadas += 1
        # p(f"Qt. de passos no Ambiente: {passos}")
        p(f"Qt. rodadas: {rodadas}")
        if cont1 > 50:
            break
            # os._exit(0)


TesteV2()
TesteV1()
graficos(ensaiosV1, ensaiosV2)

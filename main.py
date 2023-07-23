from ia_wumpus import Ambiente
from ia_wumpus import AgenteReativoV1, AgenteReativoV2
import numpy as np
import matplotlib.pyplot as plt
from ia_wumpus import __version__
from copy import deepcopy
from typing import List

plt.style.use("ggplot")

ensaiosV1: List[List] = [[], []]
ensaiosV2: List[List] = [[], []]


amb_base = Ambiente(dimensao_ambiente=35, t_pausa=0.0)
backup_amb = deepcopy(amb_base)

cont = 0
rod = 50


def graficos(ensaiosV1, ensaiosV2):
    ev1_0 = np.mean(ensaiosV1[0])
    ev1_1 = np.mean(ensaiosV1[1])
    ev2_0 = np.mean(ensaiosV2[0])
    ev2_1 = np.mean(ensaiosV2[1])

    plt.figure(figsize=(12, 6))
    plt.subplots_adjust(left=0.07, right=0.971, top=0.943, bottom=0.1,
                        wspace=0.4, hspace=0.283)

    plt.subplot(2, 1, 1)
    plt.bar([f"{i}" for i in range(len(ensaiosV1[0]))], ensaiosV1[0],
            label=f"Rodadas do Agente V1 P={ev1_0:.2f}", color="b")
    plt.bar([f"{i}" for i in range(len(ensaiosV2[0]))], ensaiosV2[0],
            linestyle='--', label=f"Rodadas do Agente V2 R={ev2_0:.2f}", color="r")
    plt.xlabel("Ensaios")
    plt.ylabel("Rodadas")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.bar([f"{i}" for i in range(len(ensaiosV1[1]))], ensaiosV1[1],
            label=f"Passos do Agente V1 P={ev1_1:.2f}", color="b")
    plt.bar([f"{i}" for i in range(len(ensaiosV2[1]))], ensaiosV2[1],
            linestyle='--', label=f"Passos do Agente V2 P={ev2_1:.2f}",
            color="r")
    plt.xlabel("Ensaios")
    plt.ylabel("passos")
    plt.legend()
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
        if cont > rod:
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
                ensaiosV2[0].append((passos))
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
        if cont1 > rod:
            break
            # os._exit(0)


TesteV2()
TesteV1()

ensaios = np.array(ensaiosV1+ensaiosV2)

np.savetxt("simulacao/sim_1_dimensao_35_v50",
           ensaiosV1+ensaiosV2, delimiter=";")
graficos(ensaiosV1, ensaiosV2)

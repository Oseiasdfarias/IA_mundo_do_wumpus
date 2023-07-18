from ia_wumpus import Ambiente
from ia_wumpus import AgenteReativoV2
from ia_wumpus import __version__
import os
from copy import deepcopy

rodadas = 0
passos = 0
amb_base = Ambiente(dimensao_ambiente=5, t_pausa=0.0)
backup_amb = deepcopy(amb_base)

while True:
    passos = 0
    amb = deepcopy(backup_amb)
    amb.mostrar_ambiente()
    agente = AgenteReativoV2(amb)
    p = agente.printw
    while True:
        agente.verificar_atirar_wumpus()

        pos_mov = agente.sortear_pos(agente.get_opcoes_mov())
        # pos_mov = agente.verificar_pos_segura()

        amb.atualiza_pos_agente(pos_mov)
        agente.pegar_outro()
        agente.verificar_morte_agente_wumpus()
        agente.verificar_morte_agente_poco()
        if agente.verificar_vitorio():
            amb.mostrar_ambiente()
            passos += 1
            rodadas += 1
            agente.ganhou_jogo()
            p(f"Versão: [blink]{__version__}[/blink]")
            p(f"Qt. de passos no Ambiente: {passos}")
            p(f"Qt. de rodadas: {rodadas}\n")
            os._exit(0)
        elif agente.morreu:
            amb.mostrar_ambiente()
            break
        passos += 1
    p(f"Qt. de passos no Ambiente: {passos}")
    rodadas += 1

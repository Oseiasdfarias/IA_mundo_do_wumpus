from ia_wumpus import Ambiente
from ia_wumpus import AgenteReativoV1
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
    agente = AgenteReativoV1(amb)
    p = agente.printw
    while True:
        agente.verificar_atirar_wumpus()
        pos_mov = agente.sortear_pos(agente.get_opcoes_mov())
        amb.atualiza_pos_agente(pos_mov)
        # amb.mostrar_ambiente()
        agente.pegar_outro()
        # agente.status_agente_ouro()
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
            break
        passos += 1
    p(f"Qt. de passos no Ambiente: {passos}")
    rodadas += 1

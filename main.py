from ia_wumpus import Ambiente
from ia_wumpus import AgenteReativoV1
import os

rodadas = 0
while True:
    amb = Ambiente()
    amb.mostrar_ambiente()
    agente = AgenteReativoV1(amb)
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
            agente.ganhou_jogo()
            print(f"Quantidade de rodadas: {rodadas}")
            os._exit(0)
        elif agente.morreu:
            break
    rodadas += 1

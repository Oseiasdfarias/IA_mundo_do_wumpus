from ia_wumpus import Ambiente
from ia_wumpus import AgenteReativoV1
from rich import print
import os

rodadas = 0
passos = 0

while True:
    passos = 0
    amb = Ambiente(dimensao_ambiente=5, t_pausa=0.0)
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
            passos += 1
            rodadas += 1
            agente.ganhou_jogo()
            print(f"[red italic bold]Qt. de passos no Ambiente: {passos}[/]")
            print(f"[red italic bold]Qt. de rodadas: {rodadas}\n[/]")
            os._exit(0)
        elif agente.morreu:
            break
        passos += 1
    print(f"[red italic bold]Qt. de passos no Ambiente: {passos}[/]")
    rodadas += 1

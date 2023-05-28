from ia_wumpus import AgenteReativoV1
from ia_wumpus import Ambiente

amb = Ambiente(dimensao_ambiente=4)
agente = AgenteReativoV1(amb)
agente.verificar_atirar_wumpus()

amb.mostrar_ambiente()
pos_mov = (0, 1)
amb.atualiza_pos_agente(pos_mov)
amb.mostrar_ambiente()
pos_mov = (0, 2)
amb.atualiza_pos_agente(pos_mov)
amb.mostrar_ambiente()
pos_mov = (0, 3)
amb.atualiza_pos_agente(pos_mov)
amb.mostrar_ambiente()
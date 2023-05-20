from ia_wumpus import Ambiente
from ia_wumpus import AgenteReativo


amb = Ambiente(dimensao_ambiente=5)
# amb.infos_ambiente()
amb.mostrar_ambiente()
# amb.mostrar_percepcoes()
amb.atualiza_pos_agente((1, 1))
amb.mostrar_ambiente()
amb.atualiza_pos_agente((2, 2))
amb.mostrar_ambiente()
amb.atualiza_pos_agente((3, 3))
amb.mostrar_ambiente()

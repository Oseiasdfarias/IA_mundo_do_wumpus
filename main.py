from ia_wumpus import Ambiente


amb = Ambiente(dimensao_ambiente=3)
amb.mostrar_ambiente()
# amb.mostrar_percepcoes()
amb.atualiza_pos_agente((1, 1))
amb.mostrar_ambiente()
amb.atualiza_pos_agente((2, 2))
amb.mostrar_ambiente()

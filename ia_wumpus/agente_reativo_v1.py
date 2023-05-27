# -----------------------------------------------------
# Universidade Federal do Pará
# Campus Universitário de Tucuruí
# Faculdade de Engenharia Elétrica
# -----------------------------------------------------
#
# Disciplina: Inteligência Computacional
# Projeto: O Mundo do Wumpus
#
# Professor: Otávio Teixeira
# Discentes: Ângelo Aragão,
#            Johanes Martins,
#            Oséias Farias
#
# Data: Maio - 2023
#  ----------------------------------------------------
from ia_wumpus import Ambiente
import os
from typing import List, Tuple


class AgenteReativoV1:
    def __init__(self, ambiente: Ambiente) -> None:
        self.amb = ambiente
        self.__list_opc_mov_ag: List = []

    def get_opcoes_mov(self) -> None:
        pos_agente = self.amb.get_pos_objetos()["agente"][0]
        self.__opcoes_mov_agente(pos_agente=pos_agente)

    def __opcoes_mov_agente(self, pos_agente: Tuple) -> None:
        """
            Verifica as possíveis opções de movimentação do agente
            para a posição atual.
        """
        self.__list_opc_mov_ag = []
        dimensao_amb = self.amb.dimensoes[0]
        if pos_agente[0] == 0:
            self.__list_opc_mov_ag.append((pos_agente[1], pos_agente[0] + 1))
        elif pos_agente[0] == (dimensao_amb - 1):
            self.__list_opc_mov_ag.append((pos_agente[1], pos_agente[0] - 1))
        elif (pos_agente[0] > 0) and (pos_agente[0] < (dimensao_amb - 1)):
            self.__list_opc_mov_ag.append((pos_agente[1], pos_agente[0] + 1))
            self.__list_opc_mov_ag.append((pos_agente[1], pos_agente[0] - 1))

        if pos_agente[1] == 0:
            self.__list_opc_mov_ag.append((pos_agente[1] + 1, pos_agente[0]))
        elif pos_agente[1] == (dimensao_amb - 1):
            self.__list_opc_mov_ag.append((pos_agente[1] - 1, pos_agente[0]))
        elif (pos_agente[1] > 0) and (pos_agente[1] < (dimensao_amb - 1)):
            self.__list_opc_mov_ag.append((pos_agente[1] + 1, pos_agente[0]))
            self.__list_opc_mov_ag.append((pos_agente[1] - 1, pos_agente[0]))

    def verificar_morte_agente_wumpus(self):
        pos_wumpus = self.amb.get_pos_objetos()["wumpus"]
        pos_agente = self.amb.get_pos_objetos()["agente"]
        print("Pos wumpus", pos_wumpus)
        print("Pos agente", pos_agente)
        for i in pos_wumpus:
            print(i)
            for j in pos_agente:
                # print(i, j)
                if i == j:
                    print("Wumpus Matou o Agente!")
                    os._exit(0)

    def verificar_morte_agente_poco(self):
        pos_wumpus = self.amb.get_pos_objetos()["pocos"]
        pos_agente = self.amb.get_pos_objetos()["agente"]
        print("Pos poco", pos_wumpus)
        print("Pos agente", pos_agente)
        for i in pos_wumpus:
            print(i)
            for j in pos_agente:
                # print(i, j)
                if i == j:
                    print("Agente caiu no poço e morreu!")
                    os._exit(0)

    def get_opcoes_mov_agente(self):
        return self.__list_opc_mov_ag

    def atirar(self) -> None:
        pass

    def mostrar_opcoes_mov(self):
        print(self.__list_opc_mov_ag)


if __name__ == "__main__":
    amb = Ambiente()
    amb.mostrar_ambiente()
    agente = AgenteReativoV1(amb)
    while True:
        agente.get_opcoes_mov()
        agente.mostrar_opcoes_mov()
        pos_mov = input("Digite a posição para se movimentar: (x, y): ")
        amb.atualiza_pos_agente(eval(pos_mov))
        amb.mostrar_ambiente()
        agente.verificar_morte_agente_wumpus()
        agente.verificar_morte_agente_poco()

    amb.atualiza_pos_agente((1, 1))
    amb.mostrar_ambiente()

    agente.get_opcoes_mov()
    agente.mostrar_opcoes_mov()

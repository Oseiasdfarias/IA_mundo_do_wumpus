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
import random

from typing import List, Tuple


class AgenteReativoV1:
    def __init__(self, ambiente: Ambiente) -> None:
        self.amb = ambiente
        self.__list_opc_mov_ag: List[Tuple] = []
        self.bala = True

    def get_opcoes_mov(self) -> List:
        pos_agente = self.amb.get_pos_objetos()["agente"][0]
        self.__opcoes_mov_agente(pos_agente=pos_agente)
        return self.__list_opc_mov_ag

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
        # print("Pos wumpus", pos_wumpus)
        # print("Pos agente", pos_agente)
        for i in pos_wumpus:
            for j in pos_agente:
                if i == j:
                    print("Wumpus Matou o Agente!")
                    os._exit(0)

    def verificar_morte_agente_poco(self):
        pos_wumpus = self.amb.get_pos_objetos()["pocos"]
        pos_agente = self.amb.get_pos_objetos()["agente"]
        # print("Pos poco", pos_wumpus)
        # print("Pos agente", pos_agente)
        for i in pos_wumpus:
            for j in pos_agente:
                # print(i, j)
                if i == j:
                    print("Agente caiu no poço e morreu!")
                    os._exit(0)

    def __sentir_fedor(self) -> bool:
        pos_agente = self.amb.get_pos_objetos()["agente"][0]
        pos_fedor = self.amb.get_percepcoes()["fedor"]
        print(pos_fedor)
        for i in pos_fedor:
            if i == pos_agente:
                print("Agente sentiu fedor")
                return True
        return False

    def sortear_item(self, opcoes):
        return random.choice(opcoes)

    def verificar_atirar_wumpus(self):
        self.get_opcoes_mov()
        if self.__sentir_fedor() and self.bala:
            self.bala = False
            pos_tiro = self.sortear_item(self.__list_opc_mov_ag)
            print("Pos tiro", pos_tiro)
            pos_wumpus = self.amb.get_pos_objetos()["wumpus"]
            for i in pos_wumpus:
                if i == pos_tiro:
                    print("Tiro e matou o Wumpos!")
                    return
            print("Errou o tiro!")

    def get_opcoes_mov_agente(self):
        return self.__list_opc_mov_ag

    def mostrar_opcoes_mov(self):
        print(self.__list_opc_mov_ag)


if __name__ == "__main__":
    amb = Ambiente()
    amb.mostrar_ambiente()
    agente = AgenteReativoV1(amb)
    while True:
        agente.verificar_atirar_wumpus()
        pos_mov = agente.sortear_item(agente.get_opcoes_mov())
        agente.mostrar_opcoes_mov()
        amb.atualiza_pos_agente(pos_mov)
        amb.mostrar_ambiente()
        agente.verificar_morte_agente_wumpus()
        agente.verificar_morte_agente_poco()

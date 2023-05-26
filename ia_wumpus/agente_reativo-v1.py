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
from typing import List, Tuple


class AgenteReativoV1:
    def __init__(self, ambiente: Ambiente) -> None:
        self.amb = ambiente
        self.__opcoes_mov_agente: List = []

    def opcoes_mov(self) -> None:
        pos_agente = self.amb.get_pos_objetos()["agente"][0]
        self.opcoes_mov_agente(pos_agente=pos_agente)

    def opcoes_mov_agente(self, pos_agente: Tuple) -> None:
        """Verifica as possíveis opções de movimentação do agente
        para a posição atual."""
        self.__opcoes_mov_agente = []
        dimensao_amb = self.amb.dimensoes[0]
        if pos_agente[0] == 0:
            self.__opcoes_mov_agente.append((pos_agente[1], pos_agente[0] + 1))
        elif pos_agente[0] == (dimensao_amb - 1):
            self.__opcoes_mov_agente.append((pos_agente[1], pos_agente[0] - 1))
        elif (pos_agente[0] > 0) and (pos_agente[0] < (dimensao_amb - 1)):
            self.__opcoes_mov_agente.append((pos_agente[1], pos_agente[0] + 1))
            self.__opcoes_mov_agente.append((pos_agente[1], pos_agente[0] - 1))

        if pos_agente[1] == 0:
            self.__opcoes_mov_agente.append((pos_agente[1] + 1, pos_agente[0]))
        elif pos_agente[1] == (dimensao_amb - 1):
            self.__opcoes_mov_agente.append((pos_agente[1] - 1, pos_agente[0]))
        elif (pos_agente[1] > 0) and (pos_agente[1] < (dimensao_amb - 1)):
            self.__opcoes_mov_agente.append((pos_agente[1] + 1, pos_agente[0]))
            self.__opcoes_mov_agente.append((pos_agente[1] - 1, pos_agente[0]))

    def get_opcoes_mov_agente(self):
        return self.__opcoes_mov_agente

    def atirar(self) -> None:
        pass

    def mostrar_opcoes_mov(self):
        print(self.__opcoes_mov_agente)


if __name__ == "__main__":
    amb = Ambiente()
    amb.mostrar_ambiente()

    agente = AgenteReativoV1(amb)
    agente.opcoes_mov()
    agente.mostrar_opcoes_mov()

    amb.atualiza_pos_agente((1, 1))
    amb.mostrar_ambiente()

    agente.opcoes_mov()
    agente.mostrar_opcoes_mov()

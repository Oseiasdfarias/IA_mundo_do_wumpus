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

import numpy as np
from random import randint
import numpy.typing as npt
from typing import Tuple, Dict


class Ambiente:
    """
        Classe que implementa o Ambiente e as percepções
        do Mundo do Wumpus.
    """
    def __init__(self, dimensao_ambiente: int = 3,
                 wumpus: int = 1, ouro: int = 1) -> None:
        if dimensao_ambiente < 3:
            self.dimensao_ambiente = 3
        else:
            self.dimensao_ambiente = dimensao_ambiente
        self.pocos = self.dimensao_ambiente
        self.wumpus = wumpus
        self.ouro = ouro
        self.dimensoes = (self.dimensao_ambiente,
                          self.dimensao_ambiente)

        self.__mundo = np.zeros(self.dimensoes, dtype=int)
        self.__mundo[:] = 0

        # Percepções dos Objetos no Ambiente.
        self.pos_percepcoes: dict = {"brisa":  [],
                                     "fedor":  [],
                                     "brilho": []}
        # Posições dos Objetos no Ambiente.
        self.pos_objetos: dict = {"pocos":  [],
                                  "wumpus": [],
                                  "ouro":   [],
                                  "agente": []}

        # Posicionando o Agente no ambiente.
        self.__add_pos_agente()
        # Posicionando o(s) Wumpu(s) no ambiente.
        self.__add_pos_wumpus()
        # Posicionando o(s) Poço(s) no ambiente.
        self.__add_pos_pocos()
        # Posicionando o(s) Ouro(s) no ambiente.
        self.__add_pos_ouro()
        # Menu
        self.__menu()

    def atualiza_pos_agente(self, pos_agente: Tuple[int, int]) -> None:
        """Atualiza a posição do Agente no Ambiente."""
        self.__mundo[self.pos_objetos["agente"][-1]] = 0
        print("antes ", self.pos_objetos["agente"][-1])
        self.pos_objetos["agente"] = [pos_agente]
        print("depois ", self.pos_objetos["agente"][-1])
        self.__mundo[self.pos_objetos["agente"][-1]] = 4

    def get_pos_objetos(self) -> Dict:
        """Obtem as posições dos Objetos no Ambiente."""
        return self.pos_objetos

    def get_percepcoes(self) -> Dict:
        """Obtem as percepções dos Objetos no Ambiente."""
        return self.pos_percepcoes

    def add_pos_obj_map(self, obj: int) -> npt.NDArray:
        """Posiciona os Objetos no Ambiente."""
        self.pos_sort = self.__sortear_pos()
        if self.__mundo[self.pos_sort[0], self.pos_sort[1]] == 0:
            self.__mundo[self.pos_sort[0], self.pos_sort[1]] = obj
            return self.pos_sort
        elif ((self.pos_sort[0] == 0) and (self.pos_sort[1] == 0)):
            self.add_pos_obj_map(obj)
        else:
            self.add_pos_obj_map(obj)
        return self.pos_sort

    def salvar_pos_objetos(self, objeto: str, pos_objeto) -> None:
        """Armazena as posições dos Objetos em um dicionário Python."""
        self.pos_objetos[objeto].append(pos_objeto)

    def __sortear_pos(self) -> npt.NDArray:
        """Sortea as posições dos Objetos no Ambiente."""
        x = randint(0, self.dimensoes[0]-1)
        y = randint(0, self.dimensoes[0]-1)
        return np.array([x, y])

    def __add_percepcoes_obj(self, objeto: str, pos: npt.NDArray) -> None:
        """Posiciona as percepções no Ambiente."""
        if pos[0] == 0:
            self.pos_percepcoes[objeto].append((pos[1], pos[0] + 1))
        elif pos[0] == (self.dimensoes[0] - 1):
            self.pos_percepcoes[objeto].append((pos[1], pos[0] - 1))
        elif (pos[0] > 0) and (pos[0] < (self.dimensoes[0] - 1)):
            self.pos_percepcoes[objeto].append((pos[1], pos[0] + 1))
            self.pos_percepcoes[objeto].append((pos[1], pos[0] - 1))

        if pos[1] == 0:
            self.pos_percepcoes[objeto].append((pos[1] + 1, pos[0]))
        elif pos[1] == (self.dimensoes[0] - 1):
            self.pos_percepcoes[objeto].append((pos[1] - 1, pos[0]))
        elif (pos[1] > 0) and (pos[1] < (self.dimensoes[0] - 1)):
            self.pos_percepcoes[objeto].append((pos[1] + 1, pos[0]))
            self.pos_percepcoes[objeto].append((pos[1] - 1, pos[0]))

    def __add_pos_wumpus(self) -> None:
        """Posicionando os Wumpo(s) no Ambiente."""
        for i in range(self.wumpus):
            pos_wumpus = self.add_pos_obj_map(1)
            self.salvar_pos_objetos(objeto="wumpus", pos_objeto=pos_wumpus)
            self.__add_percepcoes_obj(objeto="fedor", pos=pos_wumpus)
            # print(f"Wumpus pos: {pos_wumpus}")

    def __add_pos_pocos(self) -> None:
        """Posicionando os Poços no Ambiente."""
        for i in range(self.pocos):
            pos_poco = self.add_pos_obj_map(2)
            self.salvar_pos_objetos(objeto="pocos", pos_objeto=pos_poco)
            self.__add_percepcoes_obj(objeto="brisa", pos=pos_poco)
            # print(f"Poço pos: {pos_poco}")

    def __add_pos_ouro(self) -> None:
        """Posicionando o(s) Ouro(s) no Ambiente."""
        for i in range(self.ouro):
            pos_ouro = self.add_pos_obj_map(3)
            self.salvar_pos_objetos(objeto="ouro", pos_objeto=pos_ouro)
            self.pos_percepcoes["brilho"].append((pos_ouro[1], pos_ouro[0]))
            # print(f"Ouro pos: {pos_ouro}")

    def __add_pos_agente(self) -> None:
        """Posicionando o(s) Agente(s) no Ambiente."""
        self.__mundo[(0, 0)] = 4
        self.salvar_pos_objetos(objeto="agente", pos_objeto=((0, 0)))

    @classmethod
    def __menu(self) -> None:
        """Menu com a descrições dos Objetos."""
        print("\n====== Menu - Mundo do Wumpus ======")
        print("\t+ 1 - Wumpus")
        print("\t+ 2 - Poços")
        print("\t+ 3 - Ouro")
        print("\t+ 4 - Agente")
        print("====================================")

    def infos_ambiente(self) -> None:
        """Exibe a dimensão do mundo do Wumpus."""
        print(f"\nTamanho do Ambiente: {self.__mundo.shape}")

    def mostrar_ambiente(self) -> None:
        """Exibe o Mundo do Wumpus com os objetos em suas posições."""
        print(f"\nMundo do Wumpus:\n{self.__mundo}")

    def mostrar_percepcoes(self):
        """Exibe o dicionário com as posições das percepções."""
        print("\n======== Posições das Percepções - Mundo do Wumpus ========")
        print(f"\tPosição Fedor ------ :\n\t{self.pos_percepcoes['fedor']}\n")
        print(f"\tPosições Brisa ----- :\n\t{self.pos_percepcoes['brisa']}\n")
        print(f"\tPosição Brilho ----- :\n\t{self.pos_percepcoes['brilho']}")
        print("============================================================\n")


if __name__ == "__main__":
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

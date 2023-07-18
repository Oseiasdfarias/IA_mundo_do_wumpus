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
from typing import Tuple, Dict
from rich.console import Console
from rich.theme import Theme
from os import system, name
from time import sleep

custom_theme = Theme({
    "info1": "dim cyan bold",
    "color_mundo": "blue bold",
    "color_menus": "blue bold",
    "info2": "purple bold",
    "warning": "magenta",
    "green": "green",
    "danger": "red"
})
console = Console(theme=custom_theme)


class Ambiente:
    """
        Classe que implementa o Ambiente e as percepções
        do Mundo do Wumpus.
    """
    def __init__(self, dimensao_ambiente: int = 3,
                 wumpus: int = 1, ouro: int = 1,
                 t_pausa: float = 0.0) -> None:
        self.clear()
        self.t_pausa = t_pausa
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
        self.__pos_percepcoes: dict = {"brisa":  [],
                                       "fedor":  [],
                                       "brilho": [],
                                       "ouro": []}
        # Posições dos Objetos no Ambiente.
        self.__pos_objetos: dict = {"pocos":  [],
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
        if self.t_pausa < 2:
            sleep(3.0*self.t_pausa)
        else:
            sleep(3.0)

    def tempo_pausa(self):
        sleep(self.t_pausa)

    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def atualiza_pos_agente(self, pos_agente: Tuple[int, int]) -> None:
        """Atualiza a posição do Agente no Ambiente."""
        self.__mundo[self.__pos_objetos["agente"][-1]] = 0
        self.__pos_objetos["agente"] = [pos_agente]
        self.__mundo[self.__pos_objetos["agente"][-1]] = 4

    def get_pos_objetos(self) -> Dict:
        """Obtem as posições dos Objetos no Ambiente."""
        return self.__pos_objetos

    def set_pos_ouro(self) -> None:
        self.__pos_objetos["ouro"] = []

    def get_percepcoes(self) -> Dict:
        """Obtem as percepções dos Objetos no Ambiente."""
        return self.__pos_percepcoes

    def set_percepcao_ouro(self) -> None:
        self.__pos_percepcoes["brilho"] = []

    def __add_pos_obj_map(self, obj: int) -> Tuple:
        """Posiciona os Objetos no Ambiente."""
        self.pos_sort = self.__sortear_pos()
        if self.__mundo[self.pos_sort[0], self.pos_sort[1]] == 0:
            self.__mundo[self.pos_sort[0], self.pos_sort[1]] = obj
            return self.pos_sort
        elif ((self.pos_sort[0] == 0) and (self.pos_sort[1] == 0)):
            self.__add_pos_obj_map(obj)
        else:
            self.__add_pos_obj_map(obj)
        return self.pos_sort

    def __salvar_pos_objetos(self, objeto: str, pos_objeto) -> None:
        """Armazena as posições dos Objetos em um dicionário Python."""
        self.__pos_objetos[objeto].append(pos_objeto)

    def __sortear_pos(self) -> Tuple:
        """Sortea as posições dos Objetos no Ambiente."""
        x = randint(0, self.dimensoes[0]-1)
        y = randint(0, self.dimensoes[0]-1)
        return (x, y)

    def __add_percepcoes_obj(self, objeto: str, pos: Tuple) -> None:
        """Posiciona as percepções no Ambiente."""
        if pos[0] == 0:
            self.__pos_percepcoes[objeto].append((pos[1], pos[0] + 1))
        elif pos[0] == (self.dimensoes[0] - 1):
            self.__pos_percepcoes[objeto].append((pos[1], pos[0] - 1))
        elif (pos[0] > 0) and (pos[0] < (self.dimensoes[0] - 1)):
            self.__pos_percepcoes[objeto].append((pos[1], pos[0] + 1))
            self.__pos_percepcoes[objeto].append((pos[1], pos[0] - 1))

        if pos[1] == 0:
            self.__pos_percepcoes[objeto].append((pos[1] + 1, pos[0]))
        elif pos[1] == (self.dimensoes[0] - 1):
            self.__pos_percepcoes[objeto].append((pos[1] - 1, pos[0]))
        elif (pos[1] > 0) and (pos[1] < (self.dimensoes[0] - 1)):
            self.__pos_percepcoes[objeto].append((pos[1] + 1, pos[0]))
            self.__pos_percepcoes[objeto].append((pos[1] - 1, pos[0]))

    def __add_pos_wumpus(self) -> None:
        """Posicionando os Wumpo(s) no Ambiente."""
        for i in range(self.wumpus):
            pos_wumpus = self.__add_pos_obj_map(1)
            self.__salvar_pos_objetos(objeto="wumpus", pos_objeto=pos_wumpus)
            self.__add_percepcoes_obj(objeto="fedor", pos=pos_wumpus)

    def __add_pos_pocos(self) -> None:
        """Posicionando os Poços no Ambiente."""
        for i in range(self.pocos):
            pos_poco = self.__add_pos_obj_map(2)
            self.__salvar_pos_objetos(objeto="pocos", pos_objeto=pos_poco)
            self.__add_percepcoes_obj(objeto="brisa", pos=pos_poco)

    def __add_pos_ouro(self) -> None:
        """Posicionando o(s) Ouro(s) no Ambiente."""
        for i in range(self.ouro):
            pos_ouro = self.__add_pos_obj_map(3)
            self.__salvar_pos_objetos(objeto="ouro", pos_objeto=pos_ouro)
            self.__pos_percepcoes["brilho"].append((pos_ouro[1], pos_ouro[0]))
            self.__add_percepcoes_obj(objeto="ouro", pos=pos_ouro)

    def __add_pos_agente(self) -> None:
        """Posicionando o(s) Agente(s) no Ambiente."""
        self.__mundo[(0, 0)] = 4
        self.__salvar_pos_objetos(objeto="agente", pos_objeto=(0, 0))

    @staticmethod
    def __menu() -> None:
        """Menu com a descrições dos Objetos."""
        console.print("\n\n|+|+|+|+|+|+|+|+| Inicio do Jogo |+|+|+|+|+|+|+|+|",
                      style="color_menus")
        console.print("\n====== Menu - Mundo do Wumpus ======",
                      style="color_menus")
        console.print("\t+ 1 - Wumpus", style="color_menus")
        console.print("\t+ 2 - Poços", style="color_menus")
        console.print("\t+ 3 - Ouro", style="color_menus")
        console.print("\t+ 4 - Agente", style="color_menus")
        console.print("====================================",
                      style="color_menus")

    def infos_ambiente(self) -> None:
        """Exibe a dimensão do mundo do Wumpus."""
        console.print(f"\nTamanho do Ambiente: {self.__mundo.shape}",
                      style="color_mundo")

    def mostrar_ambiente(self) -> None:
        """Exibe o Mundo do Wumpus com os objetos em suas posições."""
        console.print(f"\n[gray]Mundo do Wumpus:\n{self.__mundo}",
                      style="color_mundo")
        self.tempo_pausa()

    def mostrar_percepcoes(self):
        style = "info2"
        """Exibe o dicionário com as posições das percepções."""
        console.print("\n================ Posições das Percepções =========",
                      style=style)
        console.print(f"Posição Fedor  :\n\t{self.__pos_percepcoes['fedor']}",
                      style=style)
        console.print(f"Posições Brisa :\n\t{self.__pos_percepcoes['brisa']}",
                      style=style)
        console.print(f"Posição Brilho :\n\t{self.__pos_percepcoes['brilho']}",
                      style=style)
        console.print("==================================================\n",
                      style=style)


if __name__ == "__main__":
    amb = Ambiente(dimensao_ambiente=5)
    # amb.infos_ambiente()
    amb.mostrar_ambiente()
    amb.mostrar_percepcoes()
    amb.atualiza_pos_agente((0, 1))
    amb.mostrar_ambiente()
    amb.atualiza_pos_agente((0, 2))
    amb.mostrar_ambiente()
    amb.atualiza_pos_agente((0, 3))
    amb.mostrar_ambiente()

    amb.atualiza_pos_agente((0, 4))
    amb.mostrar_ambiente()
    amb.atualiza_pos_agente((1, 4))
    amb.mostrar_ambiente()
    amb.atualiza_pos_agente((2, 4))
    amb.mostrar_ambiente()
    amb.mostrar_percepcoes()

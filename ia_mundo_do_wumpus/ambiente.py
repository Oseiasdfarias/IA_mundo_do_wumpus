import numpy as np
from random import randint
import numpy.typing as npt


class Ambiente:
    """Classe que implementa o Anbiente do Mundo do Wumpus."""
    def __init__(self, dimensao_ambiente: int = 3,
                 wumpus: int = 1, ouro: int = 1) -> None:
        self.pocos = dimensao_ambiente
        self.wumpus = wumpus
        self.ouro = ouro
        self.dimensoes = (dimensao_ambiente, dimensao_ambiente)

        self.mundo = np.zeros(self.dimensoes, dtype=int)
        self.mundo[:] = 0

        # Percepções
        self.percepcoes: dict = {"pocos":  [],
                                 "wumpus": [],
                                 "ouro":   []}

        # Posicionando o Agente no ambiente.
        self.add_pos_agente()
        # Posicionando o(s) Wumpu(s) no ambiente.
        self.add_pos_wumpus()
        # Posicionando o(s) Poço(s) no ambiente.
        self.add_pos_pocos()
        # Posicionando o(s) Ouro(s) no ambiente.
        self.add_pos_ouro()
        # Menu
        self.menu()

    def add_pos_obj(self, obj: int) -> npt.NDArray:
        """Posiciona os Objetos no Ambiente."""
        self.pos_sort = self.sortear_pos()
        if self.mundo[self.pos_sort[0], self.pos_sort[1]] == 0:
            self.mundo[self.pos_sort[0], self.pos_sort[1]] = obj
            return self.pos_sort
        elif ((self.pos_sort[0] == 0) and (self.pos_sort[1] == 0)):
            self.add_pos_obj(obj)
        else:
            self.add_pos_obj(obj)
        return self.pos_sort

    def add_percepcoes(self, objeto: str, pos: npt.NDArray) -> None:
        """Posiciona as percepções no Ambiente."""
        if pos[0] == 0:
            self.percepcoes[objeto].append((pos[1], pos[0] + 1))
        elif pos[0] == (self.dimensoes[0] - 1):
            self.percepcoes[objeto].append((pos[1], pos[0] - 1))
        elif (pos[0] > 0) and (pos[0] < (self.dimensoes[0] - 1)):
            self.percepcoes[objeto].append((pos[1], pos[0] + 1))
            self.percepcoes[objeto].append((pos[1], pos[0] - 1))

        if pos[1] == 0:
            self.percepcoes[objeto].append((pos[1] + 1, pos[0]))
        elif pos[1] == (self.dimensoes[0] - 1):
            self.percepcoes[objeto].append((pos[1] - 1, pos[0]))
        elif (pos[1] > 0) and (pos[1] < (self.dimensoes[0] - 1)):
            self.percepcoes[objeto].append((pos[1] + 1, pos[0]))
            self.percepcoes[objeto].append((pos[1] - 1, pos[0]))

    def add_pos_wumpus(self) -> None:
        """Posicionando os Wumpo(s) no Ambiente."""
        for i in range(self.wumpus):
            pos_wumpus = self.add_pos_obj(1)
            self.add_percepcoes(objeto="wumpus", pos=pos_wumpus)
            # print(f"Wumpus pos: {pos_wumpus}")

    def add_pos_pocos(self) -> None:
        """Posicionando os Poços no Ambiente."""
        for i in range(self.pocos):
            pos_poco = self.add_pos_obj(2)
            self.add_percepcoes(objeto="pocos", pos=pos_poco)
            # print(f"Poço pos: {pos_poco}")

    def add_pos_ouro(self) -> None:
        """Posicionando o(s) Ouro(s) no Ambiente."""
        for i in range(self.ouro):
            pos_ouro = self.add_pos_obj(3)
            self.add_percepcoes(objeto="ouro", pos=pos_ouro)
            # print(f"Ouro pos: {pos_ouro}")

    def sortear_pos(self) -> npt.NDArray:
        """Sortea as posições dos Objetos no Ambiente."""
        x = randint(0, self.dimensoes[0]-1)
        y = randint(0, self.dimensoes[0]-1)
        return np.array([x, y])

    @classmethod
    def menu(self) -> None:
        """Menu com a descrições dos Objetos."""
        print("\n====== Menu - Mundo do Wumpus ======")
        print("\t+ 1 - Wumpus")
        print("\t+ 2 - Poços")
        print("\t+ 3 - Ouro")
        print("\t+ 4 - Agente")
        print("====================================")

    def add_pos_agente(self) -> None:
        """Posicionando o(s) Agente(s) no Ambiente."""
        self.mundo[0, 0] = 4

    def infos_ambiente(self) -> None:
        """Exibe a dimensão do mundo do Wumpus."""
        print(f"\nTamanho do Ambiente: {self.mundo.shape}")

    def mostrar_ambiente(self) -> None:
        """Exibe o Mundo do Wumpus com os objetos em suas posições."""
        print(f"\nMundo do Wumpus:\n{self.mundo}")

    def mostrar_percepcoes(self):
        """Exibe o dicionário com as posições das percepções."""
        print("\n======== Posições das Percepções - Mundo do Wumpus ========")
        print(f"\tPos - Percepções do Wumpus:\n\t{self.percepcoes['wumpus']}\n")
        print(f"\tPos - Percepções do Poços:\n\t{self.percepcoes['pocos']}\n")
        print(f"\tPos - Percepções do Ouro:\n\t{self.percepcoes['ouro']}")
        print("============================================================\n")


if __name__ == "__main__":
    amb = Ambiente(dimensao_ambiente=3)
    # amb.infos_ambiente()
    amb.mostrar_ambiente()
    # amb.mostrar_percepcoes()

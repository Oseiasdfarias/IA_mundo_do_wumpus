import numpy as np
from random import randint


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

    def add_pos_obj(self, obj: int):
        """Posiciona os Objetos no Ambiente."""
        pos_sort = self.sortear_pos()
        if self.mundo[pos_sort[0], pos_sort[1]] == 0:
            self.mundo[pos_sort[0], pos_sort[1]] = obj
        elif pos_sort[0] == 0 and pos_sort[1] == 0:
            self.add_pos_obj(obj)
        else:
            self.add_pos_obj(obj)

    def add_pos_wumpus(self):
        """Posicionando os Wumpo(s) no Ambiente."""
        for i in range(self.wumpus):
            self.add_pos_obj(1)

    def add_pos_pocos(self):
        """Posicionando os Poços no Ambiente."""
        for i in range(self.pocos):
            self.add_pos_obj(2)

    def add_pos_ouro(self):
        """Posicionando o(s) Ouro(s) no Ambiente."""
        for i in range(self.ouro):
            self.add_pos_obj(3)

    def sortear_pos(self):
        x = randint(0, self.dimensoes[0]-1)
        y = randint(0, self.dimensoes[0]-1)
        return np.array([x, y])

    def menu(self):
        print("\n====== Menu - Mundo do Wumpus ======")
        print("\t+ 1 - Wumpus")
        print("\t+ 2 - Poços")
        print("\t+ 3 - Ouro")
        print("\t+ 4 - Agente")
        print("====================================")

    def add_pos_agente(self):
        """Posicionando o(s) Agente(s) no Ambiente."""
        self.mundo[0, 0] = 4

    def infos_ambiente(self) -> None:
        print(f"\nTamanho do Ambiente: {self.mundo.shape}")

    def mostrar_ambiente(self) -> None:
        print(f"\nMundo do Wumpus:\n{self.mundo}\n")


if __name__ == "__main__":
    amb = Ambiente(dimensao_ambiente=5)
    # amb.infos_ambiente()
    amb.mostrar_ambiente()

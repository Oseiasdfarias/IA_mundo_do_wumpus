import numpy as np
from random import randint


class Ambiente:
    """Classe que implementa o Anbiente do Mundo do Wumpus."""
    def __init__(self, dimensoes: tuple = (3, 3), poco: int = 3,
                 wumpus: int = 1, ouro: int = 1) -> None:
        self.poco = poco
        self.wumpus = wumpus
        self.ouro = ouro
        self.dimensoes = dimensoes

        self.mundo = np.chararray(dimensoes)
        self.mundo[:] = "0"
        # Posicionando o Wumpus no Mapa
        self.pos_wumpus()

        # Posicionar Agente
        self.pos_agente()

    def pos_wumpus(self):
        """Posiciona o Wumpus no Mapa!"""
        pos_sort = self.sortear_pos()
        if self.mundo[pos_sort[0], pos_sort[1]] == b"0":
            self.mundo[pos_sort[0], pos_sort[1]] = b"W"
            print(self.mundo[pos_sort[0], pos_sort[1]])
        else:
            self.pos_wumpus()

    def pos_poco(self):
        pass

    def pos_ouro(self):
        pass

    def sortear_pos(self):
        x = randint(1, self.dimensoes[0]-1)
        y = randint(1, self.dimensoes[0]-1)
        return np.array([x, y])

    def pos_agente(self):
        self.mundo[0, 0] = "A"

    def infos_ambiente(self) -> None:
        print(f"\nTamanho do Ambiente: {self.mundo.shape}")

    def mostrar_ambiente(self) -> None:
        print(f"\nMundo do Wumpus:\n{self.mundo}\n")


if __name__ == "__main__":
    amb = Ambiente((3, 3))
    amb.infos_ambiente()
    amb.mostrar_ambiente()


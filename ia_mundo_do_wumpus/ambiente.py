import numpy as np


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

        # Posicionar Agente
        self.pos_agente()

    def pos_wumpus(self):
        pass

    def pos_poco(self):
        pass

    def pos_ouro(self):
        pass

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

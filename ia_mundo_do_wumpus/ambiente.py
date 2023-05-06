import numpy as np


class Ambiente:
    """Classe que implementa o Anbiente do Mundo do Wumpus."""
    def __init__(self, dimesoes: tuple = (3, 3)) -> None:
        self.mundo = np.chararray(dimesoes)
        self.mundo[:] = "0"

    def infos_ambiente(self) -> None:
        print(f"Tamanho do Anbiente: {self.mundo.shape}")

    def mostrar_ambiente(self) -> None:
        print(f"\nMundo do Wumpus:\n{self.mundo}\n")

    def modificar_ambiente(self, pos: list = [0, 0], add: str = "x") -> None:
        self.mundo[pos[0], pos[1]] = add


if __name__ == "__main__":
    amb = Ambiente((3, 3))
    amb.infos_ambiente()
    amb.modificar_ambiente(add="W")
    amb.mostrar_ambiente()

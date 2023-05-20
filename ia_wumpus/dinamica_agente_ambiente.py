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
from ia_wumpus import AgenteReativo, Ambiente


class DinamicaAgenteAmbiente:
    def __init__(self) -> None:
        pass

    def gerar_ambiente(self):
        self.amb = Ambiente(dimensao_ambiente=5)
        # self.amb.infos_ambiente()
        self.amb.mostrar_ambiente()


if __name__ == "__main__":
    jogo = DinamicaAgenteAmbiente()
    jogo.gerar_ambiente()

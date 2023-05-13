from ia_mundo_do_wumpus import Ambiente


def run_mundo(dimensao_mundo=3):
    amb = Ambiente(dimensao_ambiente=dimensao_mundo)
    amb.mostrar_ambiente()
    # amb.mostrar_percepcoes()


if __name__ == "__main__":
    run_mundo()

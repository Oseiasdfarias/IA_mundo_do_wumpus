from ia_mundo_do_wumpus import Ambiente


def run_mundo():
    amb = Ambiente(dimensao_ambiente=3)
    # amb.infos_ambiente()
    amb.mostrar_ambiente()
    amb.mostrar_percepcoes()


if __name__ == "__main__":
    run_mundo()

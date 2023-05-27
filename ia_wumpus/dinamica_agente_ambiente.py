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
        self.amb = Ambiente(dimensao_ambiente=5)
        self.ag_reativo = AgenteReativo(self.amb)

    def pos_percepcao(self, percepcao):
        pos = self.amb.get_percepcoes[percepcao]
        return pos
    
    def verificar_agente_poco(self):
        pos_objetos = self.amb.get_pos_objetos()
        for pos in pos_objetos["poco"]:


    def verificar_percepcao_brisa(self):
        pos_brisa = self.pos_percepcao("brisa")
        pos_agente = self.amb.get_pos_objetos()
        for i in pos_brisa:
            if pos_brisa == pos_agente["agente"][0]:
                pass

    def verificar_pos_objetos(self):
        print(self.amb.get_pos_objetos())


if __name__ == "__main__":
    jogo = DinamicaAgenteAmbiente()
    jogo.verificar_pos_objetos()

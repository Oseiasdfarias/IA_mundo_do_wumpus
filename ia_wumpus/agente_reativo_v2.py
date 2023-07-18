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
from ia_wumpus import Ambiente
import os
import random
from rich.console import Console
from rich.theme import Theme
# from loguru import logger
from typing import List, Tuple

custom_theme = Theme({
    "info": "purple bold",
    "info2": "red italic bold",
    "info_bold": "purple bold",
    "warning": "yellow bold",
    "green": "green bold",
    "danger": "bold red"
})
console = Console(theme=custom_theme)


class AgenteReativoV2:
    def __init__(self, ambiente: Ambiente) -> None:
        self.amb = ambiente
        self.verificar_mov_agente()
        self.__list_opc_mov_ag: List[Tuple] = []
        self.posicao_segura: List[Tuple] = [(0, 0)]
        self.pos_anterior_agente: Tuple = (0, 0)
        self.bala: bool = True
        self.pegou_ouro: bool = False
        self.vitoria: bool = False
        self.morreu: bool = False
        self.reset = 0

    def printw(self, txt):
        console.print(txt, style="info2")

    def get_opcoes_mov(self) -> List:
        """
        Método responsável por obter as possíveis obções de movimentação
        do agente no ambiente.
        """
        pos_agente = self.amb.get_pos_objetos()["agente"][0]
        self.__opcoes_mov_agente(pos_agente=pos_agente)
        return self.__list_opc_mov_ag

    def __opcoes_mov_agente(self, pos_agente: Tuple) -> None:
        """
            Verifica as possíveis opções de movimentação do agente
            para a posição atual.
        """
        self.__list_opc_mov_ag = []
        dimensao_amb = self.amb.dimensoes[0]
        if pos_agente[0] == 0:
            self.__list_opc_mov_ag.append((pos_agente[0] + 1, pos_agente[1]))
        elif pos_agente[0] == (dimensao_amb - 1):
            self.__list_opc_mov_ag.append((pos_agente[0] - 1, pos_agente[1]))
        elif (pos_agente[0] > 0) and (pos_agente[0] < (dimensao_amb - 1)):
            self.__list_opc_mov_ag.append((pos_agente[0] + 1, pos_agente[1]))
            self.__list_opc_mov_ag.append((pos_agente[0] - 1, pos_agente[1]))

        if pos_agente[1] == 0:
            self.__list_opc_mov_ag.append((pos_agente[0], pos_agente[1] + 1))
        elif pos_agente[1] == (dimensao_amb - 1):
            self.__list_opc_mov_ag.append((pos_agente[0], pos_agente[1] - 1))
        elif (pos_agente[1] > 0) and (pos_agente[1] < (dimensao_amb - 1)):
            self.__list_opc_mov_ag.append((pos_agente[0], pos_agente[1] + 1))
            self.__list_opc_mov_ag.append((pos_agente[0], pos_agente[1] - 1))

    def removeElements(self, A, B):
        n = len(A)
        return any(A == B[i:i + n] for i in range(len(B)-n + 1))

    def verificar_mov_agente(self):
        pos_obj = self.amb.get_pos_objetos()["wumpus"] +\
                  self.amb.get_pos_objetos()["pocos"]
        print(pos_obj)
        ops = [[(0, 1), (1, 0)],
               [(1, 0), (0, 1)],
               [(1, 0), (1, 1), (0, 2)],
               [(0, 1), (1, 1), (2, 0)],
               [(0, 1), (1, 1), (2, 1)],
               [(1, 0), (1, 1), (1, 2)]]
        pos_ouro = self.amb.get_percepcoes()["ouro"]

        if all(item in pos_obj for item in pos_ouro):
            if not (self.amb.get_pos_objetos()["ouro"] == (0, 1)) or\
               not (self.amb.get_pos_objetos()["ouro"] == (1, 0)):
                print("Ambiente impossível!!!")
                os._exit(0)
        
        for i in ops:
            if all(item in pos_obj for item in i):
                print("Ambiente impossível!!!")
                print(i)
                os._exit(0)

    def verificar_morte_agente_wumpus(self) -> None:
        """
        Método responsável por verificar se o agente foi morto pelo wumpos,
        isso occore quando o agente se move para a mesma posição do wumpus.
        """
        pos_wumpus = self.amb.get_pos_objetos()["wumpus"]
        pos_agente = self.amb.get_pos_objetos()["agente"]
        for i in pos_wumpus:
            for j in pos_agente:
                if i == j:
                    # self.amb.clear()
                    console.print("\nWumpus Matou o Agente!", style="danger")
                    console.print(" \n============= Fim de Jogo =============",
                                  style="danger")
                    console.print(
                        f"[blink][b]{' '*10}DERROTA DO AGENTE [/b][/blink]",
                        style="danger")
                    console.print("=======================================\n",
                                  style="danger")
                    self.morreu = True

    def verificar_morte_agente_poco(self) -> None:
        """
        Método responsável por verificar se o agente moveu ao cair em um
        poço.
        """
        pos_wumpus = self.amb.get_pos_objetos()["pocos"]
        pos_agente = self.amb.get_pos_objetos()["agente"]
        for i in pos_wumpus:
            for j in pos_agente:
                if i == j:
                    # self.amb.clear()
                    console.print("Agente caiu no poço e morreu!",
                                  style="danger")
                    console.print(" \n============= Fim de Jogo =============",
                                  style="danger")
                    console.print(
                        f"[blink][b]{' '*10}DERROTA DO AGENTE [/b][/blink]",
                        style="danger")
                    console.print("=======================================\n",
                                  style="danger")
                    self.morreu = True

    def pegar_outro(self) -> None:
        """
        Método usado para o agente pegar o ouro caso esteja na mesma posição
        do ouro.
        """
        pos_ouro = self.amb.get_pos_objetos()["ouro"]
        pos_agente = self.amb.get_pos_objetos()["agente"]
        for i in pos_ouro:
            for j in pos_agente:
                if i == j:
                    console.print("[INFO:] Agente pegou o ouro!",
                                  style="green")
                    self.pegou_ouro = True
                    self.amb.set_percepcao_ouro()
                    self.amb.set_pos_ouro()

    def status_agente_ouro(self) -> None:
        if self.pegou_ouro:
            console.print("[INFO:] O agente está com o ouro!",
                          style="green")
        else:
            console.print("[WARN:] O agente está sem o ouro!",
                          style="warning")

    def __sentir_fedor(self) -> bool:
        pos_agente = self.amb.get_pos_objetos()["agente"][0]
        pos_fedor = self.amb.get_percepcoes()["fedor"]
        for i in pos_fedor:
            if i == pos_agente:
                console.print("[WARN:] Agente sentiu fedor",
                              style="warning")
                return True
        return False

    def __sentir_brisa(self) -> bool:
        pos_agente = self.amb.get_pos_objetos()["agente"][0]
        pos_brisa = self.amb.get_percepcoes()["brisa"]
        for i in pos_brisa:
            if i == pos_agente:
                print(i)
                print(pos_agente)
                console.print("[WARN:] Agente sentiu brisa",
                              style="warning")
                return True
        return False

    # def voltar_casa(self):

    def verificar_pos_segura(self):
        if self.pegou_ouro:
            return self.posicao_segura.pop(-1)

        elif self.amb.get_pos_objetos()["agente"] == (0, 0):
            pos_segura = self.sortear_pos(self.get_opcoes_mov())
            self.posicao_segura.append(pos_segura)
            return pos_segura

        elif self.__sentir_brisa() and self.__sentir_fedor():
            if self.reset > 3:
                pos_segura = self.sortear_pos(self.get_opcoes_mov())
                self.posicao_segura.append(pos_segura)
                self.reset = 0
                return pos_segura
            self.posicao_segura.append(self.pos_anterior_agente)
            self.reset += 1
            return self.pos_anterior_agente

        else:
            pos_segura = self.sortear_pos(self.get_opcoes_mov())
            self.posicao_segura.append(pos_segura)
            return pos_segura

    def sortear_pos(self, opcoes: List) -> Tuple[int, int]:
        return random.choice(opcoes)

    def verificar_atirar_wumpus(self) -> None:
        self.get_opcoes_mov()
        if self.__sentir_fedor() and self.bala:
            self.bala = False
            pos_tiro = self.sortear_pos(self.__list_opc_mov_ag)
            pos_wumpus = self.amb.get_pos_objetos()["wumpus"]
            for i in pos_wumpus:
                if i == pos_tiro:
                    console.print("[INFO] Atirou e matou o Wumpos!",
                                  style="green")
                    return
            console.print("[DANG] Errou o tiro!",
                          style="danger")

    def verificar_vitorio(self) -> bool:
        if self.pegou_ouro:
            if self.amb.get_pos_objetos()["agente"][0] == (0, 0):
                self.vitoria = True
        return self.vitoria

    def ganhou_jogo(self) -> None:
        if self.pegou_ouro:
            if self.amb.get_pos_objetos()["agente"][0] == (0, 0):
                console.print("\n============== Fim de Jogo ==============",
                              style="info")
                console.print(f"[blink]{' '*10}VITÓRIA DO AGENTE [/blink]",
                              style="info_bold")
                console.print("=========================================\n",
                              style="info")

    def get_opcoes_mov_agente(self) -> List:
        return self.__list_opc_mov_ag

    def mostrar_opcoes_mov(self) -> None:
        print(self.__list_opc_mov_ag)


if __name__ == "__main__":
    #    amb = Ambiente(dimensao_ambiente=5, t_pausa=0.0)
    #    amb.mostrar_ambiente()
    #    agente = AgenteReativoV2(amb)
    #    pos_mov = agente.verificar_pos_segura()
    #    amb.atualiza_pos_agente(pos_mov)
    #    amb.mostrar_ambiente()
    #
    #    pos_mov = agente.verificar_pos_segura()
    #    amb.atualiza_pos_agente(pos_mov)
    #    amb.mostrar_ambiente()
    #
    #    pos_mov = agente.verificar_pos_segura()
    #    amb.atualiza_pos_agente(pos_mov)
    #    amb.mostrar_ambiente()

    rodadas = 0
    passos = 0
    while True:
        passos = 0
        amb = Ambiente(dimensao_ambiente=5, t_pausa=0.0)
        amb.mostrar_ambiente()
        agente = AgenteReativoV2(amb)
        while True:
            agente.verificar_atirar_wumpus()
            pos_mov = agente.verificar_pos_segura()
            # pos_mov = agente.sortear_pos(agente.get_opcoes_mov())
            amb.atualiza_pos_agente(pos_mov)
            amb.mostrar_ambiente()
            agente.pegar_outro()
            agente.status_agente_ouro()
            agente.verificar_morte_agente_wumpus()
            agente.verificar_morte_agente_poco()
            if agente.verificar_vitorio():
                passos += 1
                rodadas += 1
                agente.ganhou_jogo()
                print(f"Quantidade de passos no Ambiente: {passos}")
                print(f"Quantidade de rodadas: {rodadas}\n")
                os._exit(0)
            elif agente.morreu:
                break
            passos += 1
        print(f"Quantidade de passos no Ambiente: {passos}")
        rodadas += 1
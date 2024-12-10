
from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto

class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []

        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds.keys():
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]):
        if n >= 0:
            self.noeuds[n] = coords

    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            tmp = n2
            n2 = n1
            n1 = tmp
        if n1 not in self.noeuds.keys() or n2 not in self.noeuds.keys():
            return
        if (n1, n2) not in self.arcs:
            self.arcs.append((n1, n2))

    def set_strategie(self, strat: StrategieReseau):
        self.strat = strat

    def valider_reseau(self) -> bool:
        # TODO - A tester :3
        # On va utiliser un DFS à partir du noeud d'entrée
        noeuds_visites = []
        noeuds_a_visiter = [self.noeud_entree]
        while len(noeuds_a_visiter) > 0 :
            prochain_noeud = noeuds_a_visiter.pop()
            for arc in self.arcs:
                if (arc[0] == prochain_noeud) and (arc[1] not in noeuds_visites):
                    noeuds_a_visiter.push(arc[1])
                    noeuds_visites.push(arc[1])
                elif arc[1] == prochain_noeud and (arc[0] not in noeuds_visites):
                    noeuds_a_visiter.push(arc[0])
                    noeuds_visites.push(arc[0])

        return set(noeuds_visites) == set(self.noeuds.keys())

    def valider_distribution(self, t: Terrain) -> bool:
        # TODO - A tester :3

        distrib_OK = True
        clients = t.get_clients()
        for client in clients:
            for noeud in self.noeuds:
                if client == noeud:
                    continue
            return False # Atteint uniquement si il y a un client qui n'est pas sur un noeud

        return True # Atteint uniquement si on a jamais atteint "return False"



        return False

    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs  = self.strat.configurer(t)

    def afficher(self) -> None:
        # TODO
        pass

    def afficher_avec_terrain(self, t: Terrain) -> None:
        for ligne, l in enumerate(t.cases):
            for colonne, c in enumerate(l):
                if (ligne, colonne) not in self.noeuds.values():
                    if c == Case.OBSTACLE:
                        print("X", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("~", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
                else:
                    if c == Case.OBSTACLE:
                        print("T", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("+", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
            print()

    def calculer_cout(self, t: Terrain) -> float:
        cout = 0
        for _ in self.arcs:
            cout += 1.5
        for n in self.noeuds.values():
            if t[n[0]][n[1]] == Case.OBSTACLE:
                cout += 2
            else:
                cout += 1
        return cout

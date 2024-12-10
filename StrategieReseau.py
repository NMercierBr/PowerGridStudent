
from Terrain import Terrain, Case
import os

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        print("----------------------------------- Strategie Reseau Manuelle -----------------------------------\n")
        print()
        txt = input("Veuillez choisir le fichier de terrain a charger : ")
        while not(os.path.isfile(txt)):
            txt = input(f"Le fichier {txt} n'existe pas, veuillez recommencer.")
        t.charger(txt)
        print(f"Terrain {txt} chargé.\n")
        t.afficher()
        print()
        choix = input("Souhaitez vous modifier le terrain ? Y/n \n").upper()
        entree = t.get_entree()
        noeuds = {}
        noeuds[0] = entree
        noeudcount = 0
        arcs = []
        while(choix != 'Y' and choix != 'N'):
            choix = input("Souhaitez vous modifier le terrain ? Y/n \n").upper()
        if(choix == "N"):
            return
        else :
            quit = input("Veuillez rajouter un noeud à un endroit du terrain (Entree pour continuer, X pour arreter)\n").upper()
            while(quit != 'X'):

                # On ajoute un nouveau noeud au reseau
                ligne = int(input("Ligne : "))
                colonne = int(input("Colonne : "))
                newNoeud = (ligne,colonne)
                noeudcount+=1
                
                # on vérifie que cette case n'est pas deja occupee
                if newNoeud not in noeuds.keys(): 
                    noeuds[noeudcount] = newNoeud
                else:
                    print("Ce noeud existe deja")
                    continue

                #On charge dans la liste des voisins dans choixArcs
                print(f"Les voisins du noeud ({ligne},{colonne}) sont : \n")
                tmp_choixArcs = []
                for key_noeud in noeuds.keys():
                    c = int(noeuds[key_noeud][0])
                    l = int(noeuds[key_noeud][1])
                   
                    if( ((l-1 == ligne or l+1==ligne) and (c==colonne)) or ((l==ligne) and (c-1 == colonne or c+1 == colonne))):
                        print(f"{key_noeud} : ({l},{c})\n")
                        tmp_choixArcs.append(key_noeud)

                if not tmp_choixArcs:
                    print(f"Le noeud n'a pas de voisins\n")
                else:
                    print("Veuillez choisir la liaision de votre nouveau noeud parmis :\n")
                    for val in tmp_choixArcs:
                        print(val, end=' ')
                    inputArc = input()
                    while(input not in tmp_choixArcs):
                        inputArc = input("Veuillez choisir un noeud valide !\n")
                    
                    #On prepare les valeurs de l'arc pour mettre la plus petite a gauche,
                    # la plus grande a droite, puis on creer l'arc
                    n1 = inputArc
                    n2 = noeudcount
            
                    if n1 > n2:
                        tmp = n2
                        n2 = n1
                        n1 = tmp
                    if n1 not in noeuds.keys() or n2 not in noeuds.keys():
                        return
                    if (n1, n2) not in arcs:
                        arcs.append((n1, n2))
                t.afficher()
                print()
                print(f"------------ ENTREE : {entree}")
                print(f"------------ NOEUDS : {noeuds}")
                print(f"------------ ARCS : {arcs}")
                quit = input("Veuillez rajouter un noeud à un endroit du terrain (Entree pour continuer, X pour arreter) \n").upper()

        noeuds = input()
        return entree, noeuds, arcs


class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # TODO
        return -1, {}, []



from Terrain import Terrain, Case
import os

class StrategieReseau:
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        return -1, {}, []

class StrategieReseauManuelle(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        print("----------------------------------- Strategie Reseau Manuelle -----------------------------------\n")
        print()
        txt = input("Veuillez choisir le fichier de terrain a charger : \n")
        while not(os.path.isfile(txt)):
            txt = input(f"Le fichier {txt} n'existe pas, veuillez recommencer.\n")
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
            quit = input("Souhaitez vous rajouter un noeud à un endroit du terrain ? (Entree pour continuer, X pour arreter)\n").upper()
            while(quit != 'X'):

                # on prend l'entree, en verifiant qu'on ne depasse pas du terrain
                ligne = int(input(f"Ligne (compris entre 0 et {t.hauteur-1}) : "))
                while(ligne < 0 or ligne > t.hauteur-1):
                    print("Vous depassez la taille autorisee, veuillez ressayer :\n")
                    ligne = int(input(f"Ligne (compris entre 0 et {t.hauteur-1}) : "))

                colonne = int(input(f"Colonne (compris entre 0 et {t.largeur-1}) :"))
                while(ligne < 0 or ligne > t.largeur-1):
                    print("Vous depassez la taille autorisee, veuillez ressayer :\n")
                    colonne = int(input(f"Colonne (compris entre 0 et {t.largeur-1}) :"))
                # On ajoute un nouveau noeud au reseau
                newNoeud = (ligne,colonne)
                noeudcount+=1
                
                # on vérifie que cette case n'est pas deja occupee
                if newNoeud not in noeuds.values(): 
                    noeuds[noeudcount] = newNoeud
                else:
                    print("Cette case est deja occupee par un noeud, ressayez : ")
                    continue

                #On charge dans la liste des voisins dans choixArcs
                print(f"Les voisins du noeud ({ligne},{colonne}) sont : \n")
                tmp_choixArcs = []
                for key_noeud in noeuds.keys():
                    l = int(noeuds[key_noeud][0])
                    c = int(noeuds[key_noeud][1])
                    if( ((l-1 == ligne or l+1==ligne) and (c==colonne)) or ((l==ligne) and (c-1 == colonne or c+1 == colonne))):
                        print(f"{key_noeud} : ({l},{c})\n")
                        tmp_choixArcs.append(int(key_noeud))

                if not tmp_choixArcs:
                    print(f"Le noeud n'a pas de voisins\n")
                else:
                    print("Veuillez choisir la liaision de votre nouveau noeud parmis (Entrez le numero du noeud auquel lie le nouveau noeud) :\n")
                    for val in tmp_choixArcs:
                        print(f"{val} : {noeuds[val]}\n", end=' ')
                    inputArc = int(input())
                    while(inputArc not in tmp_choixArcs):
                        inputArc = int(input("Entrez un numero de noeud valide ! \n"))
                    
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
                print()
                quit = input("Souhaitez vous rajouter un noeud à un endroit du terrain ? (Entree pour continuer, X pour arreter) \n").upper()

        return entree, noeuds, arcs


class StrategieReseauAuto(StrategieReseau):
    def configurer(self, t: Terrain) -> tuple[int, dict[int, tuple[int, int]], list[int]]:
        # TODO
        return -1, {}, []


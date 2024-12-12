
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
                
                # on vérifie que cette case n'est pas deja occupee
                if newNoeud not in noeuds.values():
                    noeudcount+=1
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
        print("----------------------------------- Strategie Reseau Automatique -----------------------------------\n")
        print()
        txt = input("Veuillez choisir le fichier de terrain a charger : \n")
        while not(os.path.isfile(txt)):
            txt = input(f"Le fichier {txt} n'existe pas, veuillez recommencer.\n")
        t.charger(txt)
        print(f"Terrain {txt} chargé.\n")
        t.afficher()
        print("\nVeuillez choisir la strategie pour generer le reseau :\n \
        \n1 : Reseau couvrant tout le terrain \
        \n2 : Reseau qui couvre toutes les lignes contenant des clients, sans prendre en compte les obstacles \
        \n3 : Algorithme optimisé \n ")

        choix = int(input())
        while (choix < 1 or choix > 3 ):
            choix = int(input("Veuillez entrer une donnee valide (entre 1 et 3) : \n"))

        #initialisation
        entree = t.get_entree()
        noeuds = {}
        noeudcount = 0
        noeuds[noeudcount] = entree
        arcs = []
        largeur = t.largeur
        hauteur = t.hauteur

        match choix:
            case 1 :    # STRATEGIE COUVRANT TOUT LE TERRAIN
                for i, li in enumerate(t.cases):
                    for j, co in enumerate(li):
                        if co == Case.ENTREE:
                            continue
                        
                        newNoeud = (i, j)
                        if newNoeud not in noeuds.values():
                            noeudcount+=1
                            noeuds[noeudcount] = newNoeud

                        for key_noeud, (l, c) in noeuds.items():
                            if (abs(l - i) == 1 and c == j) or (l == i and abs(c - j) == 1):
                                arcs.append((key_noeud, noeudcount))

            case 2 :    # STRATEGIE TOUTES LIGNES CLIENTS

                # on sonde d'abord toutes les lignes/colonnes ayant des clients
                ligne_client = []
                colonne_client = []
                for i, li in enumerate(t.cases):
                    for j, co in enumerate(li):
                        if co == Case.CLIENT :
                            ligne_client.append(i)
                            colonne_client.append(j)

                # On ajoute des noeuds sur toutes les lignes comportants des clients
                for k in ligne_client:
                    for larg in range(largeur):
                        newNoeud = (k, larg)
                        if newNoeud not in noeuds.values():
                            noeudcount+=1
                            noeuds[noeudcount] = newNoeud
                
                # On ajoute des noeuds sur toutes les colonnes comportants des clients
                for k in colonne_client:
                    for haut in range(hauteur):
                        newNoeud = (haut, k)
                        if newNoeud not in noeuds.values(): 
                            noeudcount+=1
                            noeuds[noeudcount] = newNoeud

                keys = list(noeuds.keys())

                for i in range(len(keys)):
                    key1 = keys[i]
                    x1, y1 = noeuds[key1]

                    for j in range(i + 1, len(keys)):
                        key2 = keys[j]
                        x2, y2 = noeuds[key2]

                        # Vérifier la proximité des noeuds
                        if (abs(x1 - x2) == 1 and y1 == y2) or (x1 == x2 and abs(y1 - y2) == 1):
                            arcs.append((key1, key2))

            case 3 :    # STRATEGIE ALGO OPTI
                return
            case _ :    # Erreur
                return -1

        print()
        print(f"------------ ENTREE : {entree}\n")
        print(f"------------ NOEUDS : {noeuds}\n")
        print(f"------------ ARCS : {arcs}\n")
        print(f"------------ NOMBRE D'ARCS : {len(arcs)}\n")
        print()
    
        return entree, noeuds, arcs


 
"""
Quelques fonctions python utiles ici :
- graphe comme un dictionnaire de dictionnaires pour pouvoir pondérer les arêtes:
g = {'a': {'b': 4, 'c': 2},
     'b': {'a' : 4,'d': 5, 'c': 1},
     'c': {'a' : 2, 'b' : 1, 'd' : 8,'e': 10},
     'd': {'b': 5, 'c': 8, 'e': 2},
     'e': {'c': 10, 'd' : 2, 'f': 3},
     'f': {'e' : 3,'d' : 6}}
 
- pour trouver la clé correspondant à la valeur mini d'un dictionnaire, on utilise une syntaxe très pythonesque. Par exemple, pour avoir le voisin le plus proche de 'a' :
>>> min(g['a'], key = g['a'].get)
'c'
- dict.get(cle,defaut) : retourne la valeur de cle si elle se trouve dans le dictionnaire et defaut sinon
"""


def affiche_peres(pere,depart,extremite,trajet):
    """
    À partir du dictionnaire des pères de chaque sommet on renvoie
    la liste des sommets du plus court chemin trouvé. Calcul récursif.
    On part de la fin et on remonte vers le départ du chemin.
    """
    if extremite == depart:
        return [depart] + trajet
    else:        
        return (affiche_peres(pere, depart, pere[extremite], [extremite] + trajet))
 
def plus_court(graphe,etape,fin,visites,dist,pere,depart):
    """
    Trouve récursivement la plus courte chaine entre debut et fin avec l'algo de Dijkstra
    visites est une liste et dist et pere des dictionnaires 
    graphe  : le graphe étudié                                                               (dictionnaire)
    étape   : le sommet en cours d'étude                                                     (sommet)
    fin     : but du trajet                                                                  (sommet)
    visites : liste des sommets déjà visités                                                 (liste de sommets)
    dist    : dictionnaire meilleure distance actuelle entre départ et les sommets du graphe (dict sommet : int)
    pere    : dictionnaire des pères actuels des sommets correspondant aux meilleurs chemins (dict sommet : sommet)
    depart  : sommet global de départ                                                        (sommet)
       
    """
    # si on arrive à la fin, on affiche la distance et les peres
    if etape == fin:
       return dist[fin], affiche_peres(pere,depart,fin,[])
    # si c'est la première visite, c'est que l'étape actuelle est le départ : on met dist[etape] à 0
    if len(visites) == 0: 
      dist[etape] = 0
    # on commence à tester les voisins non visités
    for voisin in graphe[etape]:
        if voisin not in visites:
            # la distance est soit la distance calculée précédemment soit l'infini
            dist_voisin = dist.get(voisin,float('inf'))
            # on calcule la nouvelle distance calculée en passant par l'étape
            candidat_dist = dist[etape] + graphe[etape][voisin]
            # on effectue les changements si cela donne un chemin plus court
            if candidat_dist < dist_voisin:
                dist[voisin] = candidat_dist
                pere[voisin] = etape
    # on a regardé tous les voisins : le noeud entier est visité
    visites.append(etape)
    # on cherche le sommet *non visité* le plus proche du départ
    non_visites = dict((s, dist.get(s,float('inf'))) for s in graphe if s not in visites)
    noeud_plus_proche = min(non_visites, key = non_visites.get)
    # on applique récursivement en prenant comme nouvelle étape le sommet le plus proche
    print(dist)
    return plus_court(graphe,noeud_plus_proche,fin,visites,dist,pere,depart)
 
def dij_rec(graphe,debut,fin):
    return plus_court(graphe,debut,fin,[],{},{},debut)


if __name__ == "__main__":

    graphe = {'a': {'b': 85, 'c': 217, 'e': 173},
          'b': {'f' : 80}, 
          'c': {'g' : 186, 'h' : 103},
          'd': {},
          'e': {'j' : 502},
          'f': {'i' : 250},
          'g': {},
          'h': {'d' : 183, 'j' : 167},
          'i': {'j' : 84},
          'j': {}
    }

    l, c = dij_rec(graphe,'a','j')
    print('\nExemple wikipedia')
    print ('Plus court chemin : ',c, ' de longueur :',l,"\n")

    graphe_oriente = {'a': {'b': 7, 'c': 9, 'f': 14},
          'b': {'c' : 10, 'd' : 15}, 
          'c': {'f' : 2, 'd' : 11},
          'd': {'e' : 6},
          'e': {'f' : 9},
          'f': {}
    }

    lgo, cgo = dij_rec(graphe_oriente,'a','e')
    print('\nGraphe orienté')
    print ('Plus court chemin : ',cgo, ' de longueur :',lgo,"\n")


    graphe_non_oriente = {'a': {'b': 7, 'c': 9, 'f': 14},
          'b': {'a' : 7, 'c' : 10, 'd' : 15}, 
          'c': {'a' : 9, 'b' : 10, 'f' : 2, 'd' : 11},
          'd': {'b' : 15, 'c' : 11, 'e' : 6},
          'e': {'d' : 6, 'f' : 9},
          'f': {'a' : 14, 'c' : 2, 'e' : 9}
    }

    lgno, cgno = dij_rec(graphe_non_oriente,'a','e')
    print('\nGraphe non orienté')
    print ('Plus court chemin : ',cgno, ' de longueur :',lgno,"\n")
 
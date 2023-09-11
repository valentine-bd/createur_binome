"""Module de gestion du programme"""
import random
import csv
from createur.membre import Membre
from createur.binome import Binome

def tirage_sans_remise(tab_tirage, n):
    """Gestion d'un tirage aléatoire sans remise"""
    tirage_ok = True
    ref_aleatoire = random.randint(1, n)

    for tirage in tab_tirage:
        if tirage == ref_aleatoire:
            tirage_ok = False
            break
        else:
            continue

    if tirage_ok is False:

        ref_aleatoire = tirage_sans_remise(tab_tirage, n)
        return ref_aleatoire

    else:

        return ref_aleatoire

def taille_groupe():
    """Détermine la taille du groupe dans le fichier membres.csv"""
    with open('csv/membres.csv', 'r', encoding='utf-8') as membre_csv:

        reader = csv.reader(membre_csv, delimiter=',')

        n = 0

        for nom in reader:
            nom
            n +=1

        return n




def creation_liste_membres():
    """Lit la totalite du fichier membres.csv et copie les données dans une liste de type membre"""
    """Associe a chaque membre une ref fixe (pour la gestion du tirage sans remise) et une ref aleatoire pour la creation des binomes"""
    ref = 1
    tab_tirage = []
    ref_aleatoire = 0
    liste_membres = []

    with open('csv/membres.csv', 'r', encoding='utf-8') as membre_csv:

        reader = csv.reader(membre_csv, delimiter=',')
        n = taille_groupe()
        print(n)

        for nom in reader:

            ref_aleatoire = tirage_sans_remise(tab_tirage, 6)
            tab_tirage.append(ref_aleatoire)

            liste_membres.append(Membre(ref, nom[0], ref_aleatoire))
            ref +=1

    return liste_membres

def tri(liste_membres):
    """Tri tous les membres de la liste par ordre croissant par rapport à leurs ref aléatoire"""
    liste_membres_triee = []
    for i in range(1, len(liste_membres)+1):
        j = 0
        while liste_membres[j].get_ref_aleatoire() != i:

            j+=1

        liste_membres_triee.append(liste_membres[j])

    return liste_membres_triee


def creation_binome(liste_membres_triee):
    """creer les binome de telle manière que le premier membre de la liste TRIEE se retrouve avec le dernier, le 2eme avec le max-1 etc... """
    for k in range(int(len(liste_membres_triee)/2)):
        n = len(liste_membres_triee)-k-1
        ref_binome = 100*liste_membres_triee[k].get_ref()+liste_membres_triee[n].get_ref()
        binome = Binome(ref_binome, liste_membres_triee[k].get_name(), liste_membres_triee[n].get_name())

        binome.write()

def affichage_liste_membres(liste_membres):
    """Affiche dans la console le contenu de la variable liste_membres"""
    for k in range(len(liste_membres)):
        liste_membres[k].affichage()
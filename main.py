"""Fonction main"""
from createur.gestion import creation_liste_membres, tri, creation_binome

# Il suffit de taper dans membres.csv les noms (ou prénoms) des élèves du groupe en allant à la ligne à chaque nom
# A chaque lancement du programme, les nouveaux binomes sont ajoutés mais n'écrasent pas les précédents.
# Il est nécéssaire de supprimer à chaque fois le fichier binome pour avoir un nouveau tirage propre
# Les refs à coté des binomes créer serviront plus tard pour gérer plusieurs tirages instantanés sans binomes en doublons.
# Lancer le programme uniquement à partir de main.py

liste = creation_liste_membres()
liste_triee = tri(liste)
creation_binome(liste_triee)

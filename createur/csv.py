import csv


def search(search_item):
    """Recherche a partir d'un item mentionne dans le fichier membres.csv"""
    with open('csv/membres.csv', 'r', encoding='utf-8') as membre_csv:

        reader = csv.reader(membre_csv, delimiter=',')

        for ligne in reader:
            for item in ligne:
                if item == search_item:
                    return ligne
                else:
                    continue
    
    print("ERREUR : Auncune correspondance dans le .csv lors de l'appel de la fonction search")

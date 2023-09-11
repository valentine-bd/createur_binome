"""Module binome"""
import csv
class Binome:
    """Classe binome"""
    def __init__(self, ref=0, membre1="", membre2=""):
        """Initialisation de la classe"""
        self.ref = ref
        self.membre1 = membre1
        self.membre2 = membre2

    def write(self):
        """Ecriture dans le csv"""
        with open('csv/binome.csv', 'a', encoding='utf-8') as binome_csv:

            writer = csv.writer(binome_csv, delimiter=',')
            ligne = [self.membre1, self.membre2, self.ref]

            writer.writerow(ligne)
            
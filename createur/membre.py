class Membre:
    """Classe membre"""
    def __init__(self, ref = 0, nom="", ref_aleatoire = 0):
        """initialisation"""
        self.ref = ref
        self.nom = nom
        self.ref_aleatoire = ref_aleatoire

    def ajout_donnees(self, donnees):
        """creer un objet membre a partir d'une ligne issue du csv membre"""
        self.ref = donnees[0]
        self.nom = donnees[1]
        self.ref_aleatoire = donnees[2]

    def get_ref(self):
        return self.ref
    
    def get_name(self):
        return self.nom
    
    def get_ref_aleatoire(self):
        return self.ref_aleatoire
    
    def affichage(self):
        print("-----")
        print("ref : ",self.ref)
        print("nom : ",self.nom)
        print("ref_aleatoire : ",self.ref_aleatoire)
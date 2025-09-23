from Cartes import *
class Joueur:
    def __init__(self,nom,score):
        self.nom = nom
        self.score = score
        self.score_tour = 0 #score du tour actuel (utilise carte bonus)

    def jouerCarte(self,carte):
        temp_score = self.score
        carte.appliquer(self) # déléguation à la méthode "appliquer"
        self.score_tour += self.score-temp_score # ajoute les points ajoutés, peut importe la carte


class Tricheur(Joueur):
    def jouerCarte(self, carte):
        if carte.carte == cartes["Malus"]:
            print(f"{self.nom} triche : il ignore le malus !") #à remove ou non
            return #coupe l'effet de la carte (ne joue pas celle-ci)
        super().jouerCarte(carte)
        
    def __init__(self, nom, score):
        super().__init__(nom, score)
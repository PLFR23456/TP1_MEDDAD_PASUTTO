from Cartes import *
class Joueur:
    def __init__(self,nom,score):
        self.nom = nom
        self.score = score
        self.last_score = 0
    def jouerCarte(self,carte):
        if(carte.carte==cartes["Bonus"]):
            #self.score *= 2
            carte.point = self.score
        carte.appliquer(self) 


class Tricheur(Joueur):
    def jouerCarte(self, carte):
        if(carte.carte==cartes["Malus"]):
            self.score += 5
        super().jouerCarte(carte)
        

    def __init__(self, nom, score):
        super().__init__(nom, score)
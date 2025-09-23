from cartes import CARTES
class Joueur:
    """Classe représentant un joueur du jeu."""
    def __init__(self,nom,score):
        """Initialise un joueur avec un nom et un score."""
        self.nom = nom
        self.score = score
        self.score_tour = 0 #score du tour actuel (utilise carte bonus)

    def jouerCarte(self,carte):
        """Joue une carte et applique son effet."""
        temp_score = self.score
        carte.appliquer(self) # déléguation à la méthode "appliquer"
        self.score_tour += self.score-temp_score # ajoute les points ajoutés, peut importe la carte


class Tricheur(Joueur):
    """Classe représentant un joueur tricheur."""
    def jouerCarte(self, carte):
        """Le tricheur ignore les cartes Malus."""
        if carte.carte == CARTES["Malus"]:
            print(f"{self.nom} triche : il ignore le malus !") #à remove ou non
            return #coupe l'effet de la carte (ne joue pas celle-ci)
        super().jouerCarte(carte)
        
    def __init__(self, nom, score):
        super().__init__(nom, score)
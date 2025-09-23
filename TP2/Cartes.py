"""Module contenant les classes de cartes du jeu (Normale, Bonus, Malus, Chance)."""
from abc import ABC, abstractmethod
import random

CARTES = {'Normale':1, 'Bonus':2, 'Malus':3, 'Chance':4}

class Carte(ABC):
    """Classe abstraite représentant une carte du jeu."""
    def __init__(self,cartes):
        """Initialise une carte générique."""
        self.carte = cartes
        self.point = None

    @abstractmethod
    def appliquer(self, joueur):
        """Applique l'effet de la carte sur le joueur."""


class CarteNormale(Carte):
    """Carte Normale : ajoute entre 1 et 10 points."""
    def __init__(self):
        super().__init__(CARTES["Normale"])
        self.point = random.randrange(1,10)
    def appliquer(self, joueur):
        joueur.score += self.point

class CarteBonus(Carte):
    """Carte Bonus : double le score du joueur."""
    def __init__(self):
        super().__init__(CARTES['Bonus'])
        self.point = 0
    def appliquer(self, joueur):
        joueur.score += joueur.score_tour

class CarteMalus(Carte):
    """Carte Malus : fait perdre 5 points au joueur."""
    def __init__(self):
        super().__init__(CARTES['Malus'])
        self.point = -5
    def appliquer(self, joueur):
        joueur.score += self.point

class CarteChance(Carte):
    """Carte Chance : ajoute ou enlève entre -5 et +15 points."""
    def __init__(self):
        super().__init__(CARTES['Chance'])
        self.point = random.randrange(-5,15)
    def appliquer(self, joueur):
        joueur.score += self.point


from abc import ABC, abstractmethod
import random

cartes = {'Normale':1, 'Bonus':2, 'Malus':3, 'Chance':4}

class Carte(ABC):
    def __init__(self,cartes):
        self.carte = cartes
        self.point = None


    @abstractmethod
    def appliquer(self, joueur):
        joueur.score += self.point




class Carte_normale(Carte):
    def __init__(self):
        self.carte = cartes['Normale']
        self.point = random.randrange(1,10)

class Carte_bonus(Carte):
    def __init__(self):
        self.carte = cartes['Bonus']
        self.point = 0

class Carte_malus(Carte):
    def __init__(self):
        self.carte = cartes['Malus']
        self.point = -5

class Carte_chance(Carte):
    def __init__(self):
        self.carte = cartes['Chance']
        self.point = random.randrange(-5,15)
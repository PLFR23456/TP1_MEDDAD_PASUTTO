from Exo2 import Position
from Exo2 import distance_simple
from Exo3 import Robot

class Cible:
    def __init__(self, pos : Position, nom : str):
        self.position = pos
        self.nom = nom
    
    def est_atteinte_par(self, robot):
        return self.position == robot.position
    
    def distance_depuis(self, robot):
        return distance_simple(robot.position.x, robot.position.y,
                               self.position.x, self.position.y,)
    
    def afficher(self):
        print(f"Cible '{self.nom}' en {self.position}")

#TESTS
cible = Cible(Position(5, 3), "Sortie")
robot = Robot(Position(2, 1))

assert cible.est_atteinte_par(robot) == False
assert cible.distance_depuis(robot) == distance_simple(2, 1, 5, 3)

print("Avant déplacement :")
robot.afficher()

robot.aller_vers(Position(5, 3))

print("Après déplacement :")
robot.afficher()

assert cible.est_atteinte_par(robot) == True  
    
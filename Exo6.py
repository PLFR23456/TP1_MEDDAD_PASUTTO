from Exo2 import Position
from Exo3 import Robot
from Exo4 import Cible
from Exo5 import Parcours

class Terrain:
    def __init__(self):
        self.robots = []
        self.parcours = None

    def ajouter_robot(self, robot):
        self.robots.append(robot)

    def definir_parcours(self, parcours):
        self.parcours = parcours

    def lancer_mission(self):
        if self.parcours is None:
            print("pas de parcours.")
            return
        for robot in self.robots:
            self.parcours.executer_parcours(robot)

    def afficher_etat(self):
        for i, robot in enumerate(self.robots, start=1):
            print(f"Robot {i}:", end="")
            robot.afficher()

#tests
terrain = Terrain()
robot1 = Robot(Position(0, 0))
robot2 = Robot(Position(1, 1))
terrain.ajouter_robot(robot1)
terrain.ajouter_robot(robot2)
parcours = Parcours()
parcours.ajouter_cible(Cible(Position(3, 3), "Objectif"))
terrain.definir_parcours(parcours)
terrain.lancer_mission()
terrain.afficher_etat()
from Exo2 import Position
from multipledispatch import dispatch
from Exo1 import distance_simple
import numpy as np

class Robot:
    def __init__ (self,pos=Position()): #SURCHARGE
        self.position = pos

    def avancer_droite(self,delta):
        self.position.x+=delta
    def avancer_haut(self,delta):
        self.position.y+=delta
    def afficher(self):
        x=self.position.x
        y=self.position.y
        print("Le robot est à la position (x=",x,", y=",y,")")

    def distance_vers_robot(self,autre_robot):
        x1=self.position.x
        y1=self.position.y
        x2=autre_robot.position.x
        y2=autre_robot.position.y
        return (distance_simple(x1,y1,x2,y2)) #on réutilise la formule de l'hypothénuse
    
    def aller_vers(self,position_cible):
        dist_x=position_cible.x-self.position.x
        dist_y=position_cible.y-self.position.y
        for i in range(abs(dist_x)):                #la consigne demande d'avancer case par case...
            self.avancer_droite(np.sign(dist_x))    # np.sign(x) renvoie -1 si x <0 et 1 sinon (et 0 si x=0)
        for i in range(abs(dist_y)):                # donc gestion de la "direction"
            self.avancer_haut(np.sign(dist_y))

#########################      3.1         ################################
robot = Robot()
robot.afficher() # Robot à position Position(x=0, y=0)
robot.avancer_droite(3)
robot.avancer_haut(4)
robot.afficher() # Robot à position Position(x=3, y=4)
robot2 = Robot(Position(6,8))
robot2.afficher() # Robot à position Position(x=6, y=8)

#########################      3.2         ################################

robot1 = Robot(Position(0, 0))
robot2 = Robot(Position(3, 4))
assert robot1.distance_vers_robot(robot2) == 5.0
robot1.aller_vers(Position(2, 3))
assert robot1.position.x == 2
assert robot1.position.y == 3
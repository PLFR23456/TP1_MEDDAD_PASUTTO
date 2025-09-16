from Exo2 import Position
from Exo3 import Robot
from Exo4 import Cible
import time

class Parcours:
    def __init__(self):
        self.list = []
    def ajouter_cible(self,cible):
        self.list.append(cible)
    def nombre_cibles(self):
        return len(self.list)
    def cible_suivante(self):
        for cible in self.list:
            if(cible.est_atteinte_par(robot) == False):
                return cible #Pas besoin de BREAK  #1ère cible non-atteinte
    def afficher(self):
        for cible in self.list:
            cible.afficher()
    def executer_parcours(self,robot):
        for cible in self.list:
            robot.aller_vers(cible.position)
            while(cible.est_atteinte_par(robot) == False):
                time.sleep(1)           # THEORIQUE car le déplacement est immédiat

#########################      5.1         ################################            
parcours = Parcours()
parcours.ajouter_cible(Cible(Position(2, 0), "Point A"))
parcours.ajouter_cible(Cible(Position(2, 3), "Point B"))
parcours.ajouter_cible(Cible(Position(5, 3), "Point C"))
assert parcours.nombre_cibles() == 3

#########################      5.2         ################################
robot = Robot()
parcours.executer_parcours(robot)
# Vérifier que le robot a atteint la dernière cible
derniere_cible = Cible(Position(5, 3), "Point C")
assert derniere_cible.est_atteinte_par(robot) == True
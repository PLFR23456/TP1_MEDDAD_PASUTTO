from Exo2 import Position
from Exo3 import Robot
from Exo4 import Cible
from Exo5 import Parcours
from Exo6 import Terrain
import os

def demonstration_complete():
    #1. Créer un terrain
    terrain = Terrain()

    #2. Ajouter 2 robots à des positions différentes
    robot1 = Robot(Position(0,0))
    robot2 = Robot(Position(1,2))
    terrain.ajouter_robot(robot1)
    terrain.ajouter_robot(robot2)

    #3. Créer un parcours avec 3 cibles
    parcours = Parcours()
    parcours.ajouter_cible(Cible(Position(1,2), "A"))
    parcours.ajouter_cible(Cible(Position(3,4), "B"))
    parcours.ajouter_cible(Cible(Position(5,3), "C"))
    terrain.definir_parcours(parcours)

    #4. Lancer la mission 
    terrain.lancer_mission()

    #5. Afficher l’état final
    os.system("cls")
    print("\nEtat final des robots :")
    terrain.afficher_etat()

#démonstration
demonstration_complete()
import numpy as np
import math
def distance_robuste(m1:float, m2:float, m3:float):
    liste = [m1,m2,m3]
    mediane=np.median(liste)
    valeur_valables=[]
    for i in liste:
        if(abs(i-mediane)/mediane < 0.5): ## Si la valeur s'écarte de - de 50% de la médiane
            valeur_valables.append(i)
    return np.average(valeur_valables)

def distance_simple(x1,y1,x2,y2): #fonction auxiliaire à cout_deplacement
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def cout_deplacement(x1,y1,x2,y2,type):
    distance = distance_simple(x1,y1,x2,y2)
    # Coûts par type de terrain :
    # — Route (R) : coût de base = distance × 1.0
    # — Herbe (H) : coût = distance × 1.5
    # — Sable (S) : coût = distance × 2.0
    # — Roche (O) : coût = distance × 3.0
    match type:
        case 'R':
            cout=distance*1.0
        case 'H':
            cout=distance*1.5
        case 'S':
            cout=distance*2.0
        case 'O':
            cout=distance*3.0
        case _:
            cout=0
    return cout

def temps_trajet(x1,y1,x2,y2,type):
    distance=distance_simple(x1,y1,x2,y2)
    # Vitesses par terrain : Route=2.0 m/s, Herbe=1.5 m/s, Sable=1.0 m/s, Roche=0.5 m/s
    match type:
        case 'R':
            vitesse = 2.0
        case 'H':
            vitesse = 1.5
        case 'S':
            vitesse = 1.0
        case 'O':
            vitesse = 0.5
        case _:
            vitesse =0
    return distance/vitesse


#########################      1.1         ################################

# Cas normal : les 3 capteurs sont cohérents
assert abs(distance_robuste(2.0, 2.1, 1.9) - 2.0) < 0.1
# Cas avec un capteur défaillant
assert abs(distance_robuste(2.0, 2.1, 15.0) - 2.05) < 0.1
# Cas limite : deux capteurs défaillants
assert abs(distance_robuste(1.0, 15.0, 20.0) - 17.5) < 0.1
# Cas extreme : tous les capteurs donnent des valeurs incohérentes
#assert distance_robuste(1.0, 15.0, 30.0) == -1 # Signale une erreur

#########################      1.2         ################################

assert cout_deplacement(0, 0, 5, 0, 'R') == 5.0 # Route horizontale
assert cout_deplacement(0, 0, 3, 4, 'H') == 7.5 # Herbe, distance=5, cout=5*1.5
assert cout_deplacement(0, 0, 0, 2, 'S') == 4.0 # Sable vertical
assert cout_deplacement(1, 1, 1, 1, 'O') == 0.0 # Pas de mouvement
                        
#########################      1.3         ################################

assert temps_trajet(0, 0, 6, 8, 'R') == 5.0 # 10m à 2m/s = 5s
assert temps_trajet(0, 0, 3, 4, 'S') == 5.0 # 5m à 1m/s = 5s
assert temps_trajet(0, 0, 0, 1, 'O') == 2.0 # 1m à 0.5m/s = 2s
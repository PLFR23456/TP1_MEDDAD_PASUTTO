from random import shuffle, randrange
from joueur import Joueur, Tricheur
from cartes import CarteNormale, CarteBonus, CarteMalus, CarteChance, CARTES
class Game:
    """Classe représentant une partie du jeu."""
    def __init__(self,nb_tours):
        """Initialise une partie avec un nombre de tours à jouer"""
        self.nb_tours=nb_tours
        self.joueurs = [] #liste nulle de joueurs
        #on utilise ici une liste et pas un dictionnaire {id : joueur()} pour un accès plus simple
        print(f"Game created players and {nb_tours} rounds")

    def add_player(self,name):
        """Ajoute un joueur à la partie."""
        for player in self.joueurs:
            # comme on utilise une liste, il nous faut une sécurité anti-doublon
            if player.nom == name :
                print(f"Player {name} already exists")
                return
        temp_player = Joueur(name,0)
        self.joueurs.append(temp_player) # le placement du joueur n'importe pas
        print(f"Player {name} added")

    def setCheater(self,name):
        """Transforme un joueur en tricheur."""
        for i in range(len(self.joueurs)):
            if self.joueurs[i].nom == name : #on tombe sur le bon car anti-doublon
                self.joueurs[i] = Tricheur(name,self.joueurs[i].score) #on "erase" le profil non-tricheur du joueur pour le remplacer par le profil Tricheur
                print(f"Player {name} is now a cheater")
                return
        print(f"Player {name} not found")

    def remplissage_deck(self):
        """Remplit et mélange le deck de cartes."""
        self.deck=[]
        deck_values = {'Normales':30,'Bonus':6,'Malus':5,'Chance':15}
        for key, value in deck_values.items():
            for _ in range(value): # boucle de remplissage du deck avec les quantités ci-dessus
                if key == 'Normales':
                    self.deck.append(CarteNormale())
                elif key == 'Bonus':
                    self.deck.append(CarteBonus())
                elif key == 'Malus':
                    self.deck.append(CarteMalus())
                elif key == 'Chance':
                    self.deck.append(CarteChance())

        shuffle(self.deck) # mélange

    def launch(self):
        """Lance la partie."""
        for tour in range(self.nb_tours):
            for player in self.joueurs:
                if len(self.deck) == 0:
                    print("No more cards in the deck!")
                    self.remplissage_deck() # on remplit le deck si jamais il est vide
                    return
                drawn_card = self.deck.pop() # pioche la carte du dessus en l'enlevant du deck
                nom_carte = list(CARTES.keys())[list(CARTES.values()).index(drawn_card.carte)] # récupère le nom de la carte en fonction de sa valeur
                print(f"Tour {tour+1} : Joueur {player.nom} tire une Carte {nom_carte}")
                player.jouerCarte(drawn_card)
                if(drawn_card.point<0):
                    print(f"Effet : Perd {abs(drawn_card.point)} points.")
                else:
                    print(f"Effet : Ajoute {drawn_card.point} points.")
                print(f"Score actuel de {player.nom} : {player.score}\n")
        for player in self.joueurs:
            print(f"Score final de {player.nom} : {player.score}")

##### MAIN #####
def main():
    jeu_1 = Game(int(input("Nombre de tours:")))
    nb_joueurs = int(input("Nombre de joueurs:"))
    for i in range(nb_joueurs):
        joueur = str(input(f"Nom du joueur {i+1}:"))
        jeu_1.add_player(joueur)
        if(randrange(1,100) == 10): # 1% de chance qu'un joueur soit un tricheur
            jeu_1.setCheater(joueur)   
    jeu_1.add_player("cheater")
    jeu_1.setCheater("cheater")  # ajoute un tricheur pour les tests
    jeu_1.remplissage_deck()
    jeu_1.launch()
    
main()
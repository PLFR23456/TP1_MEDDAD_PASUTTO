from joueur import *
from Cartes import *
class Game:
    def __init__(self,nb_tours):
        self.nb_tours=nb_tours
        self.joueurs = []
        print(f"Game created players and {nb_tours} rounds")

    def add_player(self,name):
        for player in self.joueurs:
            if(player.nom == name):
                print(f"Player {name} already exists")
                return
        temp_player = Joueur(name,0)
        self.joueurs.append(temp_player)
        print(f"Player {name} added")

    def setCheater(self,name):
        for i in range(len(self.joueurs)):
            if(self.joueurs[i].nom == name):
                self.joueurs[i] = Tricheur(name,self.joueurs[i].score)
                print(f"Player {name} is now a cheater")
                return
        print(f"Player {name} not found")
  
        

    def launch(self):
        self.deck=[]
        deck_values = {'Normales':30,'Bonus':6,'Malus':5,'Chance':15}
        for key, value in deck_values.items():
            for _ in range(value):
                if key == 'Normales':
                    self.deck.append(Carte_normale())
                elif key == 'Bonus':
                    self.deck.append(Carte_bonus())
                elif key == 'Malus':
                    self.deck.append(Carte_malus())
                elif key == 'Chance':
                    self.deck.append(Carte_chance())

        random.shuffle(self.deck)
        for tour in range(self.nb_tours):
            for player in self.joueurs:
                if len(self.deck) == 0:
                    print("No more cards in the deck!")
                    return
                
                #Tour 1 : Joueur 1 tire une Carte Chance.
                #Effet : Ajoute 10 points.
                #Score actuel de Joueur 1 : 10
                drawn_card = self.deck.pop()
                nom_carte = list(cartes.keys())[list(cartes.values()).index(drawn_card.carte)]
                print(f"Tour {tour+1} : Joueur {player.nom} tire une Carte {nom_carte}")
                player.jouerCarte(drawn_card)
                if(drawn_card.point<0):
                    print(f"Effet : Perd {drawn_card.point} points.")
                else:
                    print(f"Effet : Ajoute {drawn_card.point} points.")
                print(f"Score actuel de {player.nom} : {player.score}")
        
        for player in self.joueurs:
            print(f"Score final de {player.nom} : {player.score}")

##### MAIN #####
def main():
    jeu_1 = Game(int(input("Nombre de tours:")))
    nb_joueurs = int(input("Nombre de joueurs:"))
    for i in range(nb_joueurs):
        joueur = str(input(f"Nom du joueur {i+1}:"))
        jeu_1.add_player(joueur)
        if(random.randrange(1,100) == 10):
            jeu_1.setCheater(joueur)   
    jeu_1.add_player("cheater")
    jeu_1.setCheater("cheater")  
    jeu_1.launch()
    
main()
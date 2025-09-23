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
            print(f"--- Tour {tour+1} ---")
            for player in self.joueurs:
                if len(self.deck) == 0:
                    print("No more cards in the deck!")
                    return
                drawn_card = self.deck.pop()
                print(f"{player.nom} draws a {drawn_card.carte} card")
                player.jouerCarte(drawn_card)
                print(f"{player.nom} now has a score of {player.score}")

        
##### MAIN #####
def main():
    jeu_1 = Game(nb_tours=5)
    jeu_1.add_player("Toto")    
    jeu_1.add_player("Titi")
    jeu_1.setCheater("Titi")
    jeu_1.launch()
    
main()
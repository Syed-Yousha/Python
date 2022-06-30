"""
Implement the card game war. Rules are:

1. Deal out deck of 52 cards between two users.
2. Each player plays a card. Higher card wins. Winner takes both cards.
3. If players tie, then each player puts down three cards, and the third
   card competes.
   If a player has less than 3 cards, then they put down all of their cards
   and their final card competes against the other player's third card.
   Continue doing this until tie is broken.
   Winner takes all cards.
4. Game is over when a player doesn't have any cards. The player with
   cards remaining is the winner.
"""

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ WAR CARD GAME
import random

# useful list for creating creating cards
suite = 'H D S C'.split()
rank = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
        Will create the card deck
    """
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.deck = []

    def main_deck(self):

        for item in self.rank:

            for sym in self.suite:
                self.deck.append(sym+item)

        return self.deck

class Hand:
    """
    The hand class. the players can add or withdraw cards from here
    """

    def __init__(self,deck, deck1, deck2, user):

        self.deck = deck
        self.d1 = deck1
        self.d2 = deck2
        self.user = user

    def remove(self):
        r = random.choice(self.d1)

        if self.user == "d":
            return r
            deck1.remove(r)

        elif self.user == "e":
            deck1.append(r)
        else:
            "Error..!"

class Player():
    """
    This is the player Class. Players can check their remaining cards with its help.
    """
    def __init__(self, player, comp):
        self.player = player
        self.comp = comp

    #  \\\\\\\\\ Comparision
    def compare(self):

        print(self.player)
        print(self.comp)


        if int(self.player[1]) > int(self.comp[1]):
            print("Congrats you won the game!")

        elif int(self.player[1]) < int(self.comp[1]):
            print("Hope you'll win the second round")

        elif int(self.player[1]) == int(self.comp[1]):
            self.player = [card.remove(), card.remove(), card.remove()]
            self.comp = [card.remove(), card.remove(), card.remove()]

            print(self.player)
            print(self.comp)

            if int(self.player[0][1]) > int(self.comp[0][1]):
                print("Congrats you won the game!")
            elif int(self.player[1][1]) > int(self.comp[1][1]):
                print("Congrats you won the game!")

            elif int(self.player[2][1]) > int(self.comp[2][1]):
                print("Congrats you won the game!")
            else:
                print("Better luck next time..")


print("Welcome to Python War Card game..")
#  \\\\\\\\\\\\\\\\\\\\\\\\\ Variable

x = Deck(suite, rank)

#  Deck making

u = input("Please draw a card by pressing 'd' : ")
user = u.lower()

# Validation
if u == 'd':
    deck = x.main_deck()

    #  Handling
    deck1 = deck[:26]
    deck2 = deck[26:]
    card = Hand(deck, deck1, deck2, user)

    #  Battling
    player = card.remove()
    comp = card.remove()

    print(f" Your card is: {player}")

    # Choice to exchange
    choice = input("if you want to exchange card then type 'e' or else press 'c'  :")
    choice = choice.lower()

    if choice == "c":
        result = Player(player, comp)

    elif choice == "e":
        player = card.remove()
        result = Player(player, comp)

    else:
        print("enter a valid choice!")

    # Result
    result.compare()

else:
    print("Error!, You entered an invalid value.. ")
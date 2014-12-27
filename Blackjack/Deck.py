# Deck.py

import random 

class Deck:
    """
        This class contains a list of strings relating to card values
        (e.g. 1S = Ace of Spades, 13D = King of Diamonds). Functions in the class
        can be called to do things such as shuffle, draw_one, discard_one, etc..
    """

    def __init__(self):
        "On creation the class object will contain a list of card values"
        self.cards = [
            '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '13S',
            '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '13C',
            '1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '13H',
            '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '13D'
        ]
    
    def shuffle(self):
        "Randomly shuffle the deck list"
        random.shuffle(self.cards)

    def dealCard(self):
        "Returns and removes the last card in the deck list"
        return self.cards.pop()

    def discardFromDeck(self, num=1):
        "Removes the last card in the deck list"
        for i in range(num):
            self.cards.pop()

    def drawRandom(self):
        "Returns and removes a random card from the deck list"
        return self.cards.pop(random.randrange(len(self.cards)))

    def getCardValue(self, card):
        "Returns the int value of a card (e.g. '2D' to 2)"
        return int(card[:-1])

    def newDeck(self):
        "Returns the deck list to its original state (don't forget to shuffle!)"
        self.cards = [
            '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '13S',
            '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '13C',
            '1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '13H',
            '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '13D'
        ]

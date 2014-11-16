# deck_of_cards.py
# Class to create a deck of cards for use in card games.

import random


class Deck:
    """This class contains a list of strings relating to card values
    (e.g. 1S = Ace of Spades, 13D = King of Diamonds). Functions in the class
    can be called to do things such as shuffle, draw_one, discard_one, etc.."""

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

    def deal_one(self):
        "Returns and removes the last card in the deck list"
        return self.cards.pop()

    def view_card(self, location):
        "Valid Arguments: 'top', 'bottom', or an int value in range(0, len(self.cards))"
        if location == 'top':
            return self.cards[-1]
        elif location == 'bottom':
            return self.cards[0]
        else:
            if location == int(location) and 0 <= location < self.count():
                return self.cards[location]
            else:
                return None


    def discard_one(self):
        "Removes the last card in the deck list"
        self.cards.pop()

    def draw_random(self):
        "Returns and removes a random card from the deck list"
        return self.cards.pop(random.randrange(self.count()))

    def return_card(self, card):
        "Places a card back into the deck list at a random location"
        self.cards.insert(random.randrange(self.count()), card)        

    def list_cards(self):
        "Returns a list of all remaining cards in the deck list"
        return self.cards

    def count(self):
        "Returns the remaining number of cards in the deck"
        return len(self.cards)

    def new(self):
        "Returns the deck list to its original state (don't forget to shuffle!)"
        self.cards = [
            '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '13S',
            '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '13C',
            '1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '13H',
            '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '13D'
        ]

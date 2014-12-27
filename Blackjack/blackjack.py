# Blackjack.py

import os
from graphics import *
from Random import randrange
from Deck import Deck
from Button import Button
from Score import Score
from Player import Player

class Blackjack:

    def __init__(self, player, ai, deck, score):
        self.player = player
        self.ai = ai
        self.deck = deck
        self.score = score

    def shuffleDeck(self):
        self.deck.shuffle()

    def dealHand(self):
        for i in range(2):
            self._deal(self.player)
            self._deal(self.ai)

    def hit(self):
        self._deal(self.player)

    def stay(self):
        self._updateScore(self.player)
        self._updateScore(self.ai)
        self._aiTurn()

    def reveal(self):
        if self.score.playerWins(player.score, ai.score):
            self.player.updateHighScore(wins=1)
            return "{0} is the winner!".format(self.player.name)
        elif self.score.draw(self.score, ai.score):
            self.player.updateHighScore(draws=1)
            return "Draw"
        elif self.score.bothBusted(self.player, self.ai):
            return "You both busted!"
        else:
            self.player.updateHighScore(losses=1)
            return "ai rules, {0} is the loser!".format(self.player.name)

    def newGame(self):
        self.deck.newDeck()
        self.player.reset()
        self.ai.reset()

    def _deal(self, who):
        who.drawCard(self.deck.dealCard())

    def _updateScore(self, who):
        who.cardValues = []
        for c in who.hand:
            who.cardValues.append(self.deck.getCardValue(c))
        who.score = self.score.calculateScore(who.cardValues)

    def _aiTurn(self):
        while self.ai.score < 17:
            self._deal(self.ai)
            self._updateScore(self.ai)

if __name__ == "__main__":
    p = Player("Tony", 1, 1)
    ai = Player("ai", 2, 2)
    d = Deck()
    s = Score()
    b = Blackjack(p, ai, d, s)
    # test code here

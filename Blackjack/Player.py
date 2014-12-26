# Player.py

import os

class Player:

    def __init__(self, name, X, Y):
        self.name = name
        self.hand = []
        self.X = X
        self.Y = Y
        self.win = 0
        self.loss = 0
        self.draws = 0

    def getCard(self, card):
        self.hand.append(card)

    def hand(self):
        return self.hand

    def XY(self):
        return self.X, self.Y

    def updateX(self, default=.25):
        self.X += default

    def resetPlayer(self, X, Y):
        self.hand = []
        self.X = X
        self.Y = Y

    def updateHighScore(self, win=0, loss=0, draw=0):
        # Check if file exists
        file = open("{0}{1}HighScores{1}{2}".format(os.getcwd(), os.sep, self.name), 'w')

if __name__ == "__main__":
    # Test code here:
    p = Player("Tony", 1, 1)
    p.updateHighScore()


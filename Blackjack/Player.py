# Player.py

import os

class Player:
    """
        
    """
    def __init__(self, name, X, Y):
        "Initiate instance vairables: name, hand, X, and Y"
        self.name = name
        self.hand = []
        self.X = X  # Player specific x-axis instance variable
        self.Y = Y  # Player specific y-axis instance variable

    def getCard(self, card):
        "Adds a card to hand array"
        self.hand.append(card)

    def hand(self):
        "Returns contents of hand array"
        return self.hand

    def XY(self):
        "Returns X and Y instance variable"
        return self.X, self.Y

    def updateX(self, default=.25):
        "Update X instance variable - default set to .25"
        self.X += default

    def updateY(self, default=0):
        "Update Y instance variable - default set to 0"
        self.Y += default

    def resetPlayer(self, X, Y):
        "Resets instance variables to start a new game"
        self.hand = []
        self.X = X
        self.Y = Y

    def _getScores(self, inFile, wins, losses, draws):
        wins += int(inFile.readline()[6:-1])
        losses += int(inFile.readline()[8:-1])
        draws += int(inFile.readline()[7:-1])
        return wins, losses, draws

    def _writeToFile(self, outFile, wins, losses, draws):
        print("Wins: {0}\nLosses: {1}\nDraws: {2}".format(wins, losses, draws), file=outFile)

    def updateHighScore(self, wins=0, losses=0, draws=0):
        "Opens/Creates a file based on player name and records wins, losses, and draws"
        fName = "{0}{1}HighScores{1}{2}".format(os.getcwd(), os.sep, self.name)

        try:    # Open file if it already exists
            inFile = open(fName, "r")
            w, l, d = self._getScores(inFile, wins, losses, draws)
            inFile.close()

            outFile = open(fName, "w")
            self._writeToFile(outFile, w, l, d)
            outFile.close()

        except FileNotFoundError:   # Create file if it does not exist
            outFile = open(fName, "w")
            self._writeToFile(outFile, wins, losses, draws)
            outFile.close()


if __name__ == "__main__":
    # Test code here:

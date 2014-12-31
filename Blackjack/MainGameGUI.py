#! /usr/bin/env python3
# MainGameGUI.py

import random
import os
from graphics import *
from Deck import Deck
from Button import Button
from Score import Score
from Player import Player
from Blackjack import Blackjack


def printCardToScreen(x, y, card):
    return Image(Point(x,y), "{0}{1}cards{1}{2}.png".format(os.getcwd(), os.sep, card))

def getPlayerName():
    return name

def main():
    win = GraphWin("Cards", 1280, 915)
    win.setCoords(0, 0, 10, 10)
    Image(Point(5,5), "background.png").draw(win)
   
    
    XYLabel = [(3,9.5,"Shuffle"), (4,9.5,"Deal"), (5,9.5,"Hit"), (6,9.5,"Stay"), (7,9.5,"Reveal"), (9.5,0.5,"Quit")]
    buttons = []
    for (x,y,label) in XYLabel:
        buttons.append(Button(win,Point(x,y),.75,.75,label))
    for b in buttons:
        b.activate()

    deck = Deck()
    score = Score()
    name = getPlayerName()
    player = Player(name, 4, 4)
    ai = Player("ai", 4, 7.5)




# Quit (continuously loops through the game while the quit button has not been pressed)
p = win.getMouse()
while not buttons[5].clicked(p):


    # Shuffle
    if buttons[0].clicked(p):
        printCardToScreen(8,5.75,"rbv").draw(win)
        p = win.getMouse()


    # Deal Hand (deal two cards to the player and ai)
    elif buttons[1].clicked(p):
        # Deal player hand
        cover = card(anchor2[0], "rbv")
        cover.draw(win)
        p = win.getMouse()


    # Hit (draw a card)
    elif buttons[2].clicked(p):
        p = win.getMouse()


    # Stay (ai's hand is assessed; cards are drawn if necessary)
    elif buttons[3].clicked(p):
        p = win.getMouse()


    # Reveal (determine the winner)
    elif buttons[4].clicked(p):
        cover.undraw()
        text = Text(Point(5,5.75), winner)
        text.setSize(24)
        text.setStyle("bold")
        text.setTextColor("gold")
        text.draw(win)
        p = win.getMouse()


    else:
        p = win.getMouse()
# Close the window once 'Quit' has been pressed.
win.close()


if __name__ == '__main__':
    main()

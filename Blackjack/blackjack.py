# main.py

import random, os
from graphics import *
from deck_of_cards import Deck
from button import Button

def card(anchor, value):
    # Returns an image file equal to 'value'
    return Image(anchor, '{0}{1}cards{1}{2}.png'.format(os.getcwd(),os.sep,value))

def ai_turn(hand):
    # Evaulates the ai's hand to determine if more cards need be drawn
    # The ai plays as if it is the dealer
    value = []
    score = 0
    aces = 0
    for c in hand:
        value.append(int(c[:-1]))
    for v in value:
        if v == 1:
            aces += 1
        elif v > 10:
            v = 10
        score += v
    if 21 >= score + 10 and aces > 0:
        score += 10
        aces -= 1
    if score < 17:
        return True
    else:
        return False

def check_scores(player, ai):
    # set variables
    p_value = []
    p_score = 0
    p_aces = 0
    ai_value = []
    ai_score = 0
    ai_aces = 0
    # Evaluate player hand
    for c in player:
        p_value.append(int(c[:-1]))
    for v in p_value:
        if v == 1:
            p_aces += 1
        elif v > 10:
            v = 10
        p_score += v
    if 21 >= p_score + 10 and p_aces > 0:
        p_score += 10
        p_aces -= 1
    # Evaluate ai hand
    for c in ai:
        ai_value.append(int(c[:-1]))
    for v in ai_value:
        if v == 1:
            ai_aces += 1
        elif v > 10:
            v = 10
        ai_score += v
    if 21 >= ai_score + 10 and ai_aces > 0:
        ai_score += 10
        ai_aces -= 1
    # Return scores to be evaluated and check who won
    return p_score, ai_score

def check_win(player_score, ai_score):
    # Checks who won based on player and ai scores, then returns a string to declare the winner
    if player_score <= 21 and player_score > ai_score or player_score <= 21 and ai_score > 21:
        return 'You Win!'
    elif player_score == ai_score and player_score <= 21:
        return 'Draw'
    elif player_score > 21 and ai_score > 21:
        return 'You both busted!'
    else:
        if ai_score <= 21 and ai_score > player_score or ai_score <= 21 and player_score > 21:
            return 'Computer Wins!'

def game_loop(win):
    # Cretae Deck Object and anchor points for cards and buttons
    deck = Deck()
    anchor1 = [Point(4,4), Point(4.25,4), Point(4.5,4), Point(4.75,4), Point(5,4), Point(5.25,4), Point(5.5,4), Point(5.75,4), Point(6,4), Point(6.25,4)]
    anchor2 = [Point(4,7.5), Point(4.25,7.5), Point(4.5,7.5), Point(4.75,7.5), Point(5,7.5), Point(5.25,7.5), Point(5.5,7.5), Point(5.75,7.5), Point(6,7.5), Point(6.25,7.5)]
    anchor3 = [(3,9.5,'Shuffle'), (4,9.5,'Deal'), (5,9.5,'Hit'), (6,9.5,'Stay'), (7,9.5,'Reveal'), (9.5,0.5,'Quit')]
    # Create buttons
    buttons = []
    for (x,y,label) in anchor3:
        buttons.append(Button(win,Point(x,y),.75,.75,label))
    for b in buttons:
        b.activate()
    # Create lists to contain cards for player and ai
    player_hand = []
    ai_hand = []
    # Quit (continuously loops through the game while the quit button has not been pressed)
    p = win.getMouse()
    while not buttons[5].clicked(p):
        # Shuffle
        if buttons[0].clicked(p):
            deck.shuffle()
            card(Point(8,5.75), 'rbv').draw(win)
            p = win.getMouse()
        # Deal Hand (deal two cards to the player and ai)
        elif buttons[1].clicked(p):
            # Deal player hand
            player_hand.append(deck.deal_one())
            card(anchor1[0], player_hand[0]).draw(win)
            player_hand.append(deck.deal_one())
            card(anchor1[1], player_hand[1]).draw(win)
            # Deal ai, add 'cover' card hide first card
            ai_hand.append(deck.deal_one())
            cover = card(anchor2[0], 'rbv')
            card(anchor2[0], ai_hand[0]).draw(win)
            cover.draw(win)
            ai_hand.append(deck.deal_one())
            card(anchor2[1], ai_hand[1]).draw(win)
            p = win.getMouse()
        # Hit (draw a card)
        elif buttons[2].clicked(p):
            player_hand.append(deck.deal_one())
            card(anchor1[len(player_hand)-1], player_hand[-1]).draw(win)
            p = win.getMouse()
        # Stay (ai's hand is assessed; cards are drawn if necessary)
        elif buttons[3].clicked(p):
            while ai_turn(ai_hand):
                ai_hand.append(deck.deal_one())
                card(anchor2[len(ai_hand)-1], ai_hand[-1]).draw(win)
            p = win.getMouse()
        # Reveal (determine the winner)
        elif buttons[4].clicked(p):
            cover.undraw()
            player_score, ai_score = check_scores(player_hand, ai_hand)
            winner = check_win(player_score, ai_score)
            text = Text(Point(5,5.75), winner)
            text.setSize(24)
            text.setStyle('bold')
            text.setTextColor('gold')
            text.draw(win)
            p = win.getMouse()
        else:
            p = win.getMouse()
    # Close the window once 'Quit' has been pressed.
    win.close()

def main():
    # Create a graphics window, set coordinates, set the background image, and run the game loop
    win = GraphWin('Cards', 1280, 915)
    win.setCoords(0, 0, 10, 10)
    center = Point(5, 5)
    background = Image(center, 'background.png')
    background.draw(win)
    game_loop(win)


if __name__ == '__main__':
    main()

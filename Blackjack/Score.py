# Score.py

class Score:
    """
        Class to calculate scores and determine the outcome
        of a game of blackjack. 
    """

    def calculateScore(self, hand):
        "Takes an int array as an arguement, returns the blackjack value of the hand"
        score = 0
        aces = 0
        for c in hand:
            if c == 1:
                aces += 1
            elif c > 10:
                c = 10
            score += c
        if 21 >= (score+10) and aces > 0:
            score += 10
            aces -= 1
        return score

    def playerWins(self, player, ai):
        "Boolean return type"
        return 21 >= player > ai or player <= 21 < ai

    def draw(self, player, ai):
        "Boolean return type"
        return 21 >= player == ai

    def bothBusted(self, player, ai):
        "Boolean return type"
        return player > 21 < ai


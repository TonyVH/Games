# Score.py

class Score:
    """
        This class contains various functions to calculate scores,
        and determine the winner of a blackjack game.
    """

    def determineScore(self, hand):
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

    def determineWinner(self, p_score, ai_score):
        "Checks who won based on player and ai scores, then returns a string to declare the winner"
        if self._playerWins(p_score, ai_score):
            return "You Win!"
        elif self._draw(p_score, ai_score):
            return "Draw"
        elif self._bothBusted(p_score, ai_score):
            return "You both busted!"
        else:
            return "Computer Wins!"

    def _playerWins(self, p, a):
        return 21 >= p > a or p <= 21 < a

    def _draw(self, p, a):
        return 21 >= p == a

    def _bothBusted(self, p, a):
        return p > 21 < a


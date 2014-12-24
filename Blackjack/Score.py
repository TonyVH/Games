# Score.py

class Score:

    def evaluateHand(hand):
        cardValue = []
        score = 0
        aces = 0
        for c in hand:
            cardValue.append(int(c[:-1]))
        for v in cardValue:
            if v == 1:
                aces += 1
            elif v > 10:
                v = 10
            score += v
        if 21 >= (score+10) and aces > 0:
            score += 10
            aces -= 1
        return score

    def ai_turn(hand):
        score = evaluateHand(hand)
        return score < 17

    def playerWins(p, a):
        return p <= 21 and p > a or p <= 21 and a > 21

    def draw(p, a):
        return p == a and p <= 21

    def bothBusted(p, a):
        return p > 21 and a > 21

    def check_win(player_score, ai_score):
        # Checks who won based on player and ai scores, then returns a string to declare the winner
        if playerWins(player_score, ai_score):
            return "You Win!"
        elif draw(player_score, ai_score):
            return "Draw"
        elif bothBusted(player_score, ai_score):
            return "You both busted!"
        else:
            return "Computer Wins!"

import random
def deal_card():
    """Return a Random Card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose, opponent has blackjack"
    elif user_score==0:
        return "Win with a blackjack"
    elif user_score>21:
        return "you went over, You Lose"
    elif computer_score>21:
        return "Opponent went over, You Win"
    elif user_score>computer_score:
        return "You Win"
    else:
        return "You Lose"

def playgame():
    usercard = []
    computer_card = []
    is_gameover = False

    for _ in range(2):
        usercard.append(deal_card())
        computer_card.append(deal_card())

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    while not is_gameover:
        user_score = calculate_score(usercard)
        computer_score = calculate_score(computer_card)
        print(f"Your Cards : {usercard}, current score :{user_score}")
        print(f"computer cards : {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_gameover = True
        else:
            user_should_deal = input("Type Y to get another card, type no to pass :")
            if user_should_deal == 'y':
                usercard.append(deal_card())
            else:
                is_gameover = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your Final Hand {usercard}, Final score :{user_score}")
    print(f"Computer final hand {computer_card}, Computer Final Score :{computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play Game :")=='y':
    playgame()
import random

ROUNDS = 4

def set_cards():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    rand = []
    for i in range(ROUNDS):
        rand.append(random.choice(cards))
    return rand

def select_the_bigger(player1, player2):
    player1 = handle_string(player1)
    player2 = handle_string(player2)
    if player1 > player2:
        return 0
    elif player2 > player1:
        return 1
    else:
        return 2

def handle_string(letter):
    if letter == 'J':
        return 11
    elif letter == 'Q':
        return 12
    elif letter == 'K':
        return 13
    else:
        return letter


if __name__ == '__main__':
    print('Welcome to Ware Game')
    first_player_card = set_cards()
    print('First player cards: ', first_player_card)
    second_player_cards = set_cards()
    print('Second player cards: ', second_player_cards)
    count1 = 0
    count2 = 0
    for i in range(ROUNDS):
        winner = select_the_bigger(first_player_card[i], second_player_cards[i])
        if winner == 0:
            count1 += 1
        elif winner == 1:
            count2 += 1
    if count1 > count2:
        print("first player win!!!")
    elif count2 > count1:
        print("second player win!!!")
    else:
        print("Draw!!!")



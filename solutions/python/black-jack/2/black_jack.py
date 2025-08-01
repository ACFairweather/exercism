"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    output = 0
    if (card in ['J','Q','K']):
        output = 10
    elif (card == 'A'):
        output = 1
    else:
        output = int(card)
    return output

def higher_card(card_one, card_two):
    output = ''
    if (value_of_card(card_one) > value_of_card(card_two)):
        output = card_one
    elif (value_of_card(card_two) > value_of_card(card_one)):
        output = card_two
    else:
        output = (card_one, card_two)
    return output


def value_of_ace(card_one, card_two):
    ace = 1
    if (card_one == 'A'):
        card_one = 11
    if (card_two == 'A'):
        card_two = 11
    if (value_of_card(card_one) + value_of_card(card_two) <= 10):
        ace = 11
    return ace


def is_blackjack(card_one, card_two):
    if (card_one == 'A'):
        card_one = 11
    if (card_two == 'A'):
        card_two = 11
    return (value_of_card(card_one) + value_of_card(card_two) == 21)


def can_split_pairs(card_one, card_two):
    return (value_of_card(card_one) == value_of_card(card_two))


def can_double_down(card_one, card_two):
    return (9 <= value_of_card(card_one) + value_of_card(card_two) <= 11)
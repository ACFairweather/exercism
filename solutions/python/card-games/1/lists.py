"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
import statistics


def get_rounds(number):
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
   return statistics.median(hand) == card_average(hand) or (hand[0] + hand[-1]) / 2 == card_average(hand)


def average_even_is_average_odd(hand):
    evens = []
    odds = []
    for h in hand:
        if hand.index(h) % 2:
            odds.append(h)
        else:
            evens.append(h)
    if len(evens) and len(odds):
            return card_average(evens) == card_average(odds)
    else:
        return False
        


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
    return hand

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
    score = 0
    dice_totals = [0,0,0,0,0,0]
    for i in dice:
        dice_totals[i - 1] += 1
    if category == 7:
        if 3 in dice_totals and 2 in dice_totals:
            score = sum(dice)
    elif category == 8:
        if 4 in dice_totals:
            score = (dice_totals.index(4) + 1) * 4
        elif 5 in dice_totals:
            score = (dice_totals.index(5) + 1) * 4
    elif category == 9:
        if dice_totals == [1,1,1,1,1,0]:
            score = 30
    elif category == 10:
        if dice_totals == [0,1,1,1,1,1]:
            score = 30
    elif category == 11:
        score = sum(dice)
    elif category == 0:
        if 5 in dice_totals:
            score = 50  
    else:
        score = category * dice_totals[category - 1]
    return score
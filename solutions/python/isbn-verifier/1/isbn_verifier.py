import re

def is_valid(isbn):
    str = isbn.replace('-', '')
    num = 0
    multiplier = 10
    if len(str) == 10:
        for c in str:
            if re.match('[0-9]', c):
                c = int(c)
            elif c == 'X' and str.index(c) == len(str) - 1:
                c = 10
            else:
                return False
            num += (c * multiplier)
            multiplier -= 1
        return num % 11 == 0
    else:
        return False

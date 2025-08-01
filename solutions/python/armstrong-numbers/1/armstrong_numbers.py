def is_armstrong_number(number):
    string = str(number)
    value = 0
    for i in string:
        value += int(i) ** len(string)
    return value == number
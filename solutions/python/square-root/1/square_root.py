def square_root(number):    
    x = number / 2
    low = 0
    high = number
    while x * x != number:
        if x * x > number:
            high = x
            x = (low + high) / 2
        else:
            low = x
            x = (low + high) / 2
    return x
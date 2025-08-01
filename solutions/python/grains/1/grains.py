def square(number):
    if (number not in range(1, 65)):
        raise ValueError("square must be between 1 and 64") 
    output = 1
    for i in range(number - 1):
        output *= 2
    return output

def total():
    output = 1
    for i in range(1, 65):
         output *= 2
    return output - 1

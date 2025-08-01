def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.") 
    else:
        factors = collectFactors(number)
        return checkAliquotSum(number, factors)

def collectFactors(number):
    factors = []
    for x in range (1, number):
        if number % x == 0:
            factors.append(x)
    return factors

def checkAliquotSum(number, factors):
    total = 0
    for x in factors:
        total += x
    perfection = ''
    if total > number:
        perfection = "abundant"
    elif total == number:
        perfection = "perfect"
    else:
        perfection = "deficient"
    return perfection
        
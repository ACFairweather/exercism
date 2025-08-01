def equilateral(sides):
    a, b, c = sides
    return (triangle(sides) and a == b and b == c)


def isosceles(sides):
    a, b, c = sides
    if (triangle(sides)):
        return (a == b or a == c or b == c)
    else:
        return False


def scalene(sides):
    a, b, c = sides
    return (triangle(sides) and a != b and a != c and b != c)

def triangle(sides):
    a, b, c = sides
    return (a + b >= c and a + c >= b and b + c >= a and a > 0 and b > 0 and c > 0)

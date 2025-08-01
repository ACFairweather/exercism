def score(x, y):
    points = 0
    coords_squared = (x ** 2) + (y ** 2)
    if (coords_squared <= 1):
        points = 10
    elif (coords_squared <= 25):
        points = 5
    elif (coords_squared <= 100):
        points = 1
    return points
        

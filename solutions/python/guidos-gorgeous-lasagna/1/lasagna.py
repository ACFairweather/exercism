EXPECTED_BAKE_TIME = 40

def bake_time_remaining(time):
    """
Return elapsed cooking time.
This function takes two numbers representing the number of layers & the time already spent 
baking and calculates the total elapsed minutes spent cooking the lasagna.
"""
    return EXPECTED_BAKE_TIME - time



def preparation_time_in_minutes(layers):
    """
Return elapsed cooking time.
This function takes two numbers representing the number of layers & the time already spent 
baking and calculates the total elapsed minutes spent cooking the lasagna.
"""
    return layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
Return elapsed cooking time.
This function takes two numbers representing the number of layers & the time already spent 
baking and calculates the total elapsed minutes spent cooking the lasagna.
"""
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)

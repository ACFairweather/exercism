def egg_count(display_value):
    eggs = []
    while display_value > 0:
        eggs.insert(0, display_value % 2)
        display_value //= 2
    return eggs.count(1)

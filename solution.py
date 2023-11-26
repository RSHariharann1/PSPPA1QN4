# solution.py

def shift_orbs(orbs, factor, constant, direction, transform_after):
    if direction not in ['Left', 'Right']:
        raise ValueError("Invalid direction. Please choose 'Left' or 'Right'.")

    if transform_after not in [True, False]:
        raise ValueError("Invalid transform_after value. Please use True or False.")

    if direction == 'Left':
        orbs = shift_left(orbs)
    elif direction == 'Right':
        orbs = shift_right(orbs)

    if transform_after:
        orbs = transform_orbs(orbs, factor, constant)

    return orbs

def shift_left(orbs):
    return orbs[1:] + [orbs[0]]

def shift_right(orbs):
    return [orbs[-1]] + orbs[:-1]

def transform_orbs(orbs, factor, constant):
    transformed_orbs = [x * factor + constant if i % 2 == 0 else x + constant for i, x in enumerate(orbs)]
    return transformed_orbs

# test_solution.py

from solution import shift_orbs

def test_shift_orbs_left_transform_after():
    orbs = [3, 5, 7, 9]
    factor = 2
    constant = 3
    direction = 'Left'
    transform_after = True

    result = shift_orbs(orbs, factor, constant, direction, transform_after)

    assert result == [13, 10, 21, 6]

def test_shift_orbs_right_transform_before():
    orbs = [3, 5, 7, 9]
    factor = 2
    constant = 3
    direction = 'Right'
    transform_after = False

    result = shift_orbs(orbs, factor, constant, direction, transform_after)

    assert result == [9, 3, 5, 7]

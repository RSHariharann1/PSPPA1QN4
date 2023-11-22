from solution import shift_orbs

def test_shift_orbs_left_transform_after():
    orbs = [3, 5, 7, 9]
    factor = 2
    constant = 3
    direction = 'Left'
    transform_after = True

    result = shift_orbs(orbs, factor, constant, direction, transform_after)

    assert result == [8, 14, 12, 6]

def test_shift_orbs_right_transform_before():
    orbs = [3, 5, 7, 9]
    factor = 2
    constant = 3
    direction = 'Right'
    transform_after = False

    result = shift_orbs(orbs, factor, constant, direction, transform_after)

    assert result == [8, 12, 6, 14]

def test_shift_orbs_invalid_direction():
    orbs = [3, 5, 7, 9]
    factor = 2
    constant = 3
    direction = 'InvalidDirection'
    transform_after = True

    try:
        shift_orbs(orbs, factor, constant, direction, transform_after)
    except ValueError as e:
        assert str(e) == "Invalid direction. Please choose 'Left' or 'Right'."

def test_shift_orbs_invalid_transform_after():
    orbs = [3, 5, 7, 9]
    factor = 2
    constant = 3
    direction = 'Left'
    transform_after = 'InvalidValue'

    try:
        shift_orbs(orbs, factor, constant, direction, transform_after)
    except ValueError as e:
        assert str(e) == "Invalid transform_after value. Please use True or False."

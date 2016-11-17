def nums_with_while(increment_to, increment_by):
    i = 0
    numbers = []
    while i < increment_to:
        numbers.append(i)
        i += increment_by

    return numbers


def nums_with_range(increment_to, increment_by):
    return range(0, increment_to, increment_by)


assert (nums_with_while(6, 1) == nums_with_range(6, 1))
assert (nums_with_while(37, 3) == nums_with_range(37, 3))

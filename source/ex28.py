assert (True and True) is True
assert (False and True) is False
assert (1 == 1) is True
assert (1 == 2) is False
assert ("test" == "test") is True
assert (1 == 1 or 2 != 1) is True
assert (True and 1 == 1) is True
assert (False and 0 != 0) is False
assert (True or 1 == 1) is True
assert ("test" == "testing") is False
assert (1 != 0 and 2 == 1) is False
assert ("test" == 1) is False
assert (not (True and False)) is True
assert (not (1 == 1 and 0 != 1)) is False
assert (not (10 == 1 and 1000 == 1000)) is True
assert (not (1 != 10 or 3 == 4)) is False
assert (not ("testing" == "testing" and "Zed" == "Cool Guy")) is True
assert (1 == 1 and not ("testing" == 1 or 1 == 0)) is True
assert ("chunky" == "bacon" and not (3 == 4 or 3 == 3)) is False
assert (3 == 3 and not ("testing" == "testing" and "python" == "fun")) is True


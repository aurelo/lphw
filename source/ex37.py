"""
Keywords
"""
# FROM AS
from sys import argv as arguments
script = arguments

# AND
if True and True:
    print True

# DEL - Deletion of a name removes the binding of that name from the local or global namespace
dummy = "Hello"
print dummy
del dummy
# print dummy # gives error - dummy no longer exists

# NOT
if not False:
    print True

# GLOBAL
global_variable = 0


def true_global():
    global global_variable
    global_variable= 42


# YIELD - for generator functions that series of values
#       - is for generator functions what return is for "normal" functions
#       - saves state of generator function
#       - we get the next value of generator function by using next() -> implicit in for loop
def yield_generator_function_example():
    yield 1
    yield 2
    yield 3


for i in yield_generator_function_example():
    print i

my_generator = yield_generator_function_example()
print next(my_generator)
print next(my_generator)
print next(my_generator)

# LAMBDA -> anonymous function
sumation = lambda x, y: x + y
print "SUM:", sumation(1, 2)

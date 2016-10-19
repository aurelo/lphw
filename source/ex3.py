# PEMDAS => Parentheses Exponents Multiplication Division Addition Subtraction ~ Python order of operations
print "I will now count my chickens!"
print "Hens", 25 + 30 / 6  # operator precedence -> / is evaluated before +
print "Roosters", 100 - 25 * 3 % 4  # operators: "*" and "%" of the same precedence, evaluated left to right

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6  # precision lost on 1 / 4
print 3 + 1.0 / 4  # use floating point numbers not to lose precision (with decimal dot)

print "Is it true that 3 + 2 < 5 - 7", 3 + 2 < 5 - 7  # for comparison arguments evaluated before operation
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7
print "Oh. that's why it's False"

print "How about some more?"

print "Is it greater", 5 > -2
print "Is it greater or equal", 5 >= -2
print "Is it less or equal", 5 <= -2

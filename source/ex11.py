# comma will force the user input inline with question, and will prevent print to end with new line chr
'''
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()
'''
#  raw_input([prompt]) => If the prompt argument is present, it is written to standard output without a trailing newline
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So you're %r old, %r tall and %r heavy" % (age, height, weight)
# int will try to convert to integer
print "So you're %s old, %s tall and %s heavy" % (int(age), height, weight)

def print_two(*argv):
    arg1, arg2 = argv
    print "First: %r, second: %r" % (arg1, arg2)


def print_two_again(arg1, arg2):
    print "First: %r, second: %r" % (arg1, arg2)
    print arg1 + arg2


def print_one(arg1):
    print "Only argument: %r" % arg1


def print_none():
    print "I got none"


print_two("One", "Two")
print_two_again("One", "Two")
print_one("Lonely")
print_none()

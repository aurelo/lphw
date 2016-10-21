from sys import argv

script, first, second = argv

print "The script is called", script
print "First argument is", first
print "Second argument is", second

missing= raw_input("What you forgot: ")

print "Entered: ", missing

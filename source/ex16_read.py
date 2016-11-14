from sys import argv

script, filename = argv

print "Current content of the file: %r" % filename

target = open(filename)
for line in target:
    print line

from sys import argv
from os.path import exists

script, in_file, out_file = argv

print "Copying from %r to %r" % (in_file, out_file)

print "Does the out file exists? %r" % exists(out_file)
print "Ready, hit RETURN to continue, CTRL-C to abort!"

raw_input()

open(out_file, 'w').write(open(in_file).read());

print "Alright, all done!"

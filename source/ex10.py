# escape sequences

tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\a\\ cat"
fat_cat = """
I'll do a list:
\t* cat food
\t* fish
\t* catnip\n\t* grass
"""


print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print '\\ => backslash'
print '\' => single quote'
print "\" => double quote"
print "\a => ascii BEL"
print "\b => ascii backspace (BS)"
print "\f => ascii form feed (FF)"
print "\n => ascii linefeed (FF)"
print "\r => ascii carriage return (CR)"
print "\t => ascii horizontal tab"
print u"Hello\u0020world => character with 16 bit hex value xxxx ~ in this example space is 0020"
print "\v => ascii vertical tab"

# comma on the end prevents print to go on new line, and \r is CR
# TODO purpose of this exercise?
for i in ["/", "-", "|", "\\", "|"]:
    print "%s\r" % i,

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                       "With pockets full of shells"])

happy_bday.sing()
bulls_on_parade.sing()

lyrics = ["I backed my car into a cop car the other day", "Well, he just drove off - sometimes life's okay"]
float_on = Song(lyrics)
float_on.sing()

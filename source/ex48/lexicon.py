default_directions = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
default_verbs = ["go", "stop", "kill", "eat"]
default_stop_words = ["the", "in", "of", "from", "at", "it", "and"]
default_nouns = ["door", "bear", "princess", "cabinet"]


def scan(sentence, direction=default_directions, verb=default_verbs, stop_words=default_stop_words,
         nouns=default_nouns):

    words = []

    for word in sentence.split():

        if str.lower(word) in direction:
            words.append(('direction', word))

        elif str.lower(word) in verb:
            words.append(('verb', word))

        elif str.lower(word) in stop_words:
            words.append(('stop', word))

        elif str.lower(word) in nouns:
            words.append(('noun', word))

        elif str.lower(word).isdigit():
            words.append(('number', word))

        else:
            words.append(('error', word))

    return words

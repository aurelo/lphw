def gold_room():
    print "This room is full of gold! How much do you take?"

    action = raw_input('> ')
    how_much = None

    if action.isdigit():
        how_much = int(action)
    else:
        dead("Man, learn to type a number!")

    if how_much < 50:
        print "Nice, you're not greedy! You win!"
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"

    bear_moved = False

    while True:
        action = raw_input("> ")
        if action == 'take honey':
            dead("The bear looks at you, then slaps your face off!")
        elif action == 'taunt bear' and not bear_moved:
            print "The bear has moved from the door! You can go through it now."
            bear_moved = True
        elif action == 'taunt bear' and bear_moved:
            gold_room()
        else:
            print "I have no idea what that means!"


def cthulhu_room():
    print "Here you see a great evil Cthulhu"
    print "He, it, whatever, stares at you until you go insane"
    print "Do you flee for your life, or eat your head?"

    action = raw_input("> ")

    if 'flee' in action:
        start()
    elif 'head' in action:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(message):
    print message, "Good job!"
    exit(0)


def start():
    print "You are in dark room."
    print "There is a door to your left and your right."
    print "Which one do you take?"

    next_room = raw_input("> ")
    if next_room == 'left':
        bear_room()
    elif next_room == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve!")


start()

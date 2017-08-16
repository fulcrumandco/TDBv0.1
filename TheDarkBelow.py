from sys import exit
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element
import random
from random import randint, choice

error_list = ["I didn't understand that.", "What are you saying?", "That doesn't compute.", "Dude, what.", "You aren't making sense.", "That's highly illogical."]
inventory = []
area = ""



def restart():
    print "Would you like to try again?"

    next = raw_input("> ")

    if next == "yes":
        start()
    else:
        print("You have surrendered to the darkness. Better luck next time!")
        exit(0) 

def dead(why):
    print why, "The end!"
    restart()

def quit():
    print "Are you sure you'd like to quit?"

    next = raw_input("> ")

    if next == "yes":
        print("You have surrendered to the darkness. Better luck next time!")
    else:
        pass

# Game start and room 1

def start():
    description = """
    You stand before a glowing portal of shimmering opal, which
    appears to be carved directly into the cliff face. It is surrounded
    on all sides by hideous gargoyles and ornate statues depicting the 
    heroes who have come before you. The portal wavers, beckoning you to
    step forward and enter into the depths it conceals.\n"""
    print description
    print "Do you step into the portal?"
    
    while True:
        next = raw_input("> ")

        if next == "yes":
            print "You step forward into the portal, and a cold wave washes over you."
            entry()
        elif next == "no":
            print "Fear clutches at you, and you step back from the portal."
            dead("""
            With a small 'pop', the portal vanishes, leaving you surrounded by
            high cliffs and steep walls. You shiver as the wind picks up, and look
            around for a way to start a fire... eventually, the light from the clifftop
            fades away.""")
        elif next == "look":
            print description
        elif next == "quit":
            dead("You have surrendered to the darkness. Better luck next time!")
        else:
            print "Yes or no, adventurer."


# Room 2. Connects to Dwelling and Altar. Items: Torch. Light mechanic to be added later.     
def entry():
    area = "entry"
    description = """
    The portal spits you out into a large, dark room, lit only by a single torch.
    It looks like you could pry the torch off the wall. Dim flickers of light
    come from two different passages, one to your left and one to your right.
    """
    print description

    while True:
        next = raw_input("> ")

        if "left" in next:
            print "You head off to the left, through the rough-hewn tunnel."
            print "It appears to have grotesque paintings on the walls - monsters flash"
            print "in the torchlight. The dark gives you a chill."
            altar()
        elif "right" in next:
            print "You head off to the right, into the darker, narrower passage."
            print "The path ahead is littered with small bones, and a smell rises in your"
            print "nostrils. Something rotten floats on the air in this corridor."
            dwelling()
        elif next == "look":
            print description
        elif next == "take torch":
            inventory.append("Torch")
            print "After some effort, the torch breaks free of the sconce holding it to the wall. You take it."
        else:
            print(random.choice(error_list))

# Room 3. Connects to Entry and Empty Hall.
# Items: Knife and Potion. Need description and elif for "look at altar".
def altar():
    description = '''
    There is an altar of bones standing before you, with crude pewter icons.
    There is painting on the walls, in what looks like blood. 
    The path continues forward, into the dark, and back the way you came.'''
    knife_taken = False
    bottle_taken = False
    print description

    # Next section looks for knife and bottle objects (not official objects) and if the player has
    # taken them already or not. This is a good example of why this needs to be rewritten, since
    # it has to be coded in to the "look" option below, as well. There's a better way to do this.
    if knife_taken == False:
        print "    Something shiny gleams on top of the gruesome surface."
    else:
        pass
    if bottle_taken == False:
        print "    There is a small bottle of something dark sitting on the bones."
    else:
        pass

    while True:
        next = raw_input("> ")

        if "look at bottle" in next:
            print "The bottle appears to be filled with a murky, smooth  substance the color of blood. Do you take it?"

            answer = raw_input("> ")
            if answer == "yes":
                inventory.append("Potion")
                bottle_taken = True
                print "You take the bottle."
            else:
                print "You leave the bottle on the altar."
        elif "look at" in next:
            print "The object appears to be a knife. Do you take it?"

            answer = raw_input("> ")
            if answer == "yes":
                inventory.append("Knife")
                knife_taken = True
                print "You take the knife."
            else:
                print "You leave the knife on the altar."
        elif next == "look":
            print description
            if knife_taken == False:
                print "Something shiny gleams on top of the gruesome surface."
            else:
                pass
            if bottle_taken == False:
                print "There is a small bottle of something dark sitting on the bones."
            else:
                pass
        elif next == "go forward":
            print "You step forward into the dark tunnel, wondering where you will pop out next."
            empty_hall()
        elif next == "go back":
            entry()
        else:
            print(random.choice(error_list))

# Room 4. No items here. Connects to Kitchen and Entry.
def dwelling():
    description = """
    The room you enter appears to be some kind of living space. The low ceiling has a small hole in
    it, which appears to go all the way to the surface. There are a couple small beds against one wall.
    The room appears empty aside from the beds. 
    """

# Room 5. No items here. Connects to altar and Large Hall.
def empty_hall():
    description = """

    """



print "Welcome, Adventurer!"
start()

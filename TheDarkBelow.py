from sys import exit
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element
from tkFileDialog import askopenfilename
import random
from random import randint, choice

error_list = ["I didn't understand that.", "What are you saying?", "That doesn't compute.", "Dude, what.", "You aren't making sense.", "That's highly illogical."]
inventory = []

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
        continue


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
            
def entry():
    description = """
    The portal spits you out into a large, dark room, lit only by a single torch.
    It looks like you could pry the torch off the wall. Dim flickers of light
    come from two different passages, one to your left and one to your right.
    """
    print description

    while True:
        next = raw_input("> ")

        if next == "go left":
            print "You head off to the left, through the rough-hewn tunnel."
            print "It appears to have grotesque paintings on the walls - monsters flash"
            print "in the torchlight. The dark gives you a chill."
            altar()
        elif next == "go right":
            print "You head off to the right, into the darker, narrower passage."
            print "The path ahead is littered with small bones, and a smell rises in your"
            print "nostrils. Something rotten floats on the air in this corridor."
            dwelling()
        elif next == "look":
            print description
        elif next == "take torch":
            inventory.append("torch")
            print "After some effort, the torch breaks free of the sconce holding it to the wall. You take it."
        else:
            print(random.choice(error_list))

def altar():
    description = '''
    There is an altar of bones standing before you, with crude pewter icons.
    There is painting on the walls, in what looks like blood. 
    Something shiny gleams on top of the rough surface. The path continues forward, into the dark,
    and back the way you came.'''
    print description

    while True:
        next = raw_input("> ")

        if "look at" in next:
            print "The object appears to be a knife. Do you take it?"

            answer = raw_input("> ")
            if answer == "yes":
                inventory.append("knife")
                print "You take the knife."
            else:
                print "You leave the knife on the altar."
        elif next == "look":
            print description
        elif next == "go forward":
            print "You step forward into the dark tunnel, wondering where you will pop out next."
            empty_hall()
        elif next == "go back":
            entry()
        else:
            print(random.choice(error_list))


# def dwelling():
print "Welcome, Adventurer!"
start()
#!/usr/bin/env python

# Rogerbot

import chatServer as c
import random

def setup():
    c.output("Hello, my name is Roger.")
    c.sleep(1) #wacht 1 seconde tot het volgende antwoord verschijnt
    c.output('What is up')

def response(input):
    #print(input)
    if respondToTrigger(input):
        pass
    else:
        c.output(randomResponse())

def randomResponse():
    answers = [
        "OK",
        "okay"
    ]
    return random.choice(answers)

def randomAssignment():
    answers = [
        "the assignment is to design a chatbot",
        "design a chatbot",
        "a chatbot, you make it!",
        "make it work, this chatbot",
    ]
    return random.choice(answers)

def respondToTrigger(input):
    triggers = ["assignment", "opdracht", "what do i do"]
    for t in triggers:
        if t in input:
            c.output(randomAssignment())
            return True
    return False
#dus wanneer het woord 'assignment' gebruikt wordt in de input
#van een persoon in de chatbot, herkent de code dit woord en
#reageert met de zin "the assignment is...": intelligent chatbot

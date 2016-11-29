#!/usr/bin/env python

# Default bot template

from chatServer import as c

def setup():
    c.output("This is the bot template.")
    c.sleep(1)
    c.output('It does nothing more than just responding with "Ok".')

def response(input):
    print(input)
    c.output("Ok")

def respondRandom():
    answers = [
        "OK",
        "Roger",
        "Roger that",
        "Acknowleged",
        "Confirmative"
    ]
    c.output()

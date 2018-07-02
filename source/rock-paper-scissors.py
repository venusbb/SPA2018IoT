# Rock, Paper, Scissors
# by Maisie Fernandes
from microbit import *
import random

rock = Image("00000:"
             "06660:"
             "06660:"
             "77777:"
             "77777")

paper = Image("88888:"
              "88888:"
              "88888:"
              "88888:"
              "88888")

scissor = Image("80008:"
                "08080:"
                "00800:"
                "08080:"
                "80008")

answers = [rock, paper, scissor]

display.show("GO!")
while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(1000)
        display.show(random.choice(answers))

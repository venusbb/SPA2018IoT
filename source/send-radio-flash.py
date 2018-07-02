# A micro:bit Firefly.
# By Nicholas H.Tollervey. Released to the public domain.
from microbit import *
import radio

radio.on()
radio.config(channel=17)        # Choose your own channel number
#radio.config(power=7)           # Turn the signal up to full strength

# Event loop.
while True:
    if button_a.was_pressed():
        radio.send('flash')
        sleep(500)

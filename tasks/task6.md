# Task 6 : Firefly

## Aim

In this task we’re going to use the radio module to create something akin to a swarm of fireflies signalling to each other. We want to create virtual fireflies using multiple micro:bits (each micro:bit acts as a firefly).

## Goal

First use your micro:bit to transmit the signal to those around you and them transmitting the signal to those around them. 

Then modify the example code below to make your Micro:bit flash randomly.

## Instructions

### Example Code
```python
# A micro:bit Firefly.
# By Nicholas H.Tollervey. Released to the public domain.
import radio
import random
from microbit import display, Image, button_a, sleep

# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# The radio won't work unless it's switched on.
radio.on()

# Event loop.
while True:
    # Button A sends a "flash" message.
    if button_a.was_pressed():
        radio.send('flash')  # a-ha
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == 'flash':
        # If there's an incoming "flash" message display
        # the firefly flash animation after a random short
        # pause.
        sleep(random.randint(50, 350))
        display.show(flash, delay=100, wait=False)
        # Randomly re-broadcast the flash message after a
        # slight delay.
        if random.randint(0, 9) == 0:
            sleep(500)
            radio.send('flash')  # a-ha
```

### Supporting information

* The complete tutorial and technical documentation about using the radio functions to mimic the firefly behaviour can be found [here](https://microbit-micropython.readthedocs.io/en/latest/tutorials/radio.html#fireflies).
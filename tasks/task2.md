# Task 2 : Buttons

## Aim

This exercise aims to expose the usage of the buttons on a micro:bit.

## Goal

Implement the logic so that:
* Press Button A - Display a heart
* Press Button B - Display a message

## Instructions

### Buttons on your micro:bit
There are two buttons on the board called `button_a` and `button_b`. 

### Library functions
`is_pressed()` - Returns True if the specified button is pressed, and False otherwise.

`was_pressed()` - Returns True or False to indicate if the button was pressed since the device started or the last time this method was called.

`get_presses()` - Returns the running total of button presses, and resets this total to zero before returning.

### Example Code
```python
from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll("AB")
        break
    elif button_a.is_pressed():
        display.scroll("A")
    elif button_b.is_pressed():
        display.scroll("B")
    sleep(100)
```

### Supporting information

* The complete tutorial and technical documentation about Buttons can be found [here](http://microbit-micropython.readthedocs.io/en/latest/button.html).
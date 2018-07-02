# Task 4 : Movement and Gestures

## Aim

This exercise aims to expose the integration of movements and gestures in a micro:bit.

## Goal

### Simple movement and gestures
Try out the accelerometer tilt and shake detection functions on your micro:bit. 

### Playing rock paper scissors
Pair with your partner to create a rock paper scissors game by shaking the micro:bit. 

Use the tasks 3 example to create your own images for each and share the code with your partner to have a go at the game.

## Instructions

### Movement
Your BBC micro:bit comes with an accelerometer. It measures movement along three axes:
* X - tilting from left to right.
* Y - tilting forwards and backwards.
* Z - moving up and down.

### Gestures
MicroPython is able to recognise the following gestures: `up`, `down`, `left`, `right`, `face up`, `face down`, `freefall`, `3g`, `6g`, `8g`, `shake`. 

Gestures are always represented as strings. While most of the names should be obvious, the `3g`, `6g` and `8g` gestures apply when the device encounters these levels of g-force (like when an astronaut is launched into space).

### Example Code

There is a method for each axis that returns a positive or negative number indicating a measurement in milli-g’s. When the reading is 0 you are “level” along that particular axis.
For example, here’s a very simple spirit-level that uses get_x to measure how level the device is along the X axis:

```python
from microbit import *

while True:
    reading = accelerometer.get_x()
    if reading > 20:
        display.show("R")
    elif reading < -20:
        display.show("L")
    else:
        display.show("-")
```

## Supporting information

* The complete tutorial and technical documentation about Movement can be found [here](http://microbit-micropython.readthedocs.io/en/latest/tutorials/movement.html).

* The complete tutorial and technical documentation about Gestures can be found [here](http://microbit-micropython.readthedocs.io/en/latest/tutorials/gestures.html).

:arrow_forward: Go to [next task](task5.md)
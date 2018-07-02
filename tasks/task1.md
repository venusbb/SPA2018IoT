# Task 1 : Hello World!

## Aim

This is the simpliest exercise to get you started with:
* writing some Python code
* using the online editor
* shipping the code to the micro:bit and seeing it in action 

## Goal

Implement the logic so that the text `Hello, World!` scrolls pass on your micro:bit and a heart is displayed. The sequence repeats after 2 seconds.

## Instructions

Copy the following example code from the online editor onto the Micro:bit.

```python
from microbit import * 

while True:
    display.scroll('Hello, World!')
    display.show(Image.HEART)
    sleep(2000)
```

Download the hex file and ship it onto your micro:bit.

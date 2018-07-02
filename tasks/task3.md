# Task 3 : Images


## Aim

This exercise aims to expose the usage of the creating and displaying images on a micro:bit.

## Goal

Implement the logic so that you can display customised images on a micro:bit.

## Instructions

The `Image` class is used to create images that can be displayed easily on the device’s LED matrix. Given an image object it’s possible to display it via the display API:

```python
display.show(Image.HAPPY)

class microbit.Image(string)
class microbit.Image(width=None, height=None, buffer=None)
```

If `string` is used, it has to consist of digits 0-9 arranged into lines, describing the image, for example the following code will create a 5×5 image of an X. :

```
from microbit import *

image = Image("90009:"
              "09090:"
              "00900:"
              "09090:"
              "90009")
display.show(image)
```

## Supporting information

* The complete tutorial and technical documentation about Images can be found [here](http://microbit-micropython.readthedocs.io/en/latest/image.html).
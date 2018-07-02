# Task 5 : Radio

## Aim

Wireless interaction is all about physics: radio waves (a type of electromagnetic radiation, similar to visible light) have some sort of property (such as their amplitude, phase or pulse width) modulated by a transmitter in such a way that information can be encoded and, thus, broadcast. When radio waves encounter an electrical conductor (i.e. an aerial), they cause an alternating current from which the information in the waves can be extracted and transformed back into its original form.

Your micro:bit has a radio chip that can be used to transmit and receive messages.

This exercise aims to expose the usage of radio broadcasting and receiving features in a micro:bit.

*Challenge: How do you ensure you are only receiving messages from your partner?*

## Goal

Working with you partner, use the radio broadcasting and receiving feature in conjunction with channl config to broadcast your group number to everyone using the Radio library.

## Instructions

### Example Code - switching the radio on/off:
```python
radio.on() # Switch the radio on.
```

### Example Code - setting a channel number:
```python
radio.config(channel=19) # Set the channel number to 19
```

### Example Code - setting the power level:
```python
radio.config(power=7) # Set the power level to 7
```

### Example Code - sending a message:
```python
from microbit import *
import radio

radio.on()

# Event loop.
while True:
    if button_a.was_pressed():
        radio.send('flash')
        sleep(500)
```

### Example Code - receiving a message:
```python
from microbit import *
import radio

radio.on()

# Event loop.
while True:
    
    incoming = radio.receive()
        if incoming == 'flash':
            display.show(incoming)
            print(incoming)
    sleep(500)
```

### Troubleshooting: 
If you print the incoming message, you will see that sometimes it contains the value `None`. That is because sometimes the micro:bit checks for a message but nothing has arrived. We can ignore these non-events by checking whether incoming equals `None` and ignoring it if that is the case. (Just make sure your partner is not sending you a string with value `None`!)

### Supporting information

* The complete tutorial and technical documentation about Radio can be found [here](http://microbit-micropython.readthedocs.io/en/latest/radio.html).
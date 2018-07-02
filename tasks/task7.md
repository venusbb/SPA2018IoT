# Task 7 : Firefly (Part 2)

## Aim

Fireflies start with random blinking. However as time goes by, they slowly synchronize with their nearest neighbors. These neighbors are synchronizing themselves with their neighbors and so on until the whole tree or the whole valley blinks in the same cycle. 

This is used to attract other specimen. With all the blinking in sync, it is much easier to find a partner.

See [here](https://ncase.me/fireflies/) for a demonstration of what it looks like.

*Challenge: What happens if one micro:bit has the lowest power transmission and the other is much set to the highest? Walk around the room to understand the impact of this.*

## Goal

Modify the code from [task 6](task6.md) to get your micro:bits to synchronise periodically.

## Instructions

The issue with radio is that you can’t transmit directly to one person. Anyone with an appropriate aerial can receive the messages you transmit. As a result it’s important to be able to differentiate who should be receiving broadcasts.

Modify the code further by configuring the radio transmission range:

```python
radio.on()
radio.config(power=0)
```
# What is in this directory?
There are six tasks in total:

* [Task 1 : Hello World!](task1.md)
* [Task 2 : Buttons](task2.md)
* [Task 3 : Images](task3.md)
* [Task 4 : Movement and Gestures](task4.md)
* [Task 5 : Radio](task5.md)
* [Task 6 : Firefly](task6.md)

# Quick links:

* [Python online editor](http://python.microbit.org/v/1)
* [micro:bit Python library quick reference](http://microbit-micropython.readthedocs.io/en/latest/index.html)

# Error handling cheat sheet

This is where things get fun and MicroPython tries to be helpful. If it encounters an error it will scroll a helpful message on the micro:bit’s display. If it can, it will tell you the line number for where the error can be found.

* `NameError` - If MicroPython complains about a NameError it’s probably because you’ve typed something inaccurately.

* `SyntaxError` - If MicroPython complains about a SyntaxError you’ve simply typed code in a way that MicroPython can’t understand. Check you’re not missing any special characters like " or :.

* *micro:bit stops responding* - For example you cannot flash new code to it or enter commands into the REPL. If this happens, try power cycling it. That is, unplug the USB cable (and battery cable if it’s connected), then plug the cable back in again. You may also need to quit and restart your code editor application.

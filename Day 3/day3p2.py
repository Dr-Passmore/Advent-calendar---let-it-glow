from machine import Pin
import time

redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

while True:
    if redbutton.value() == 1:
        print("Red Button pressed!")
    if greenButton.value() == 1:
        print("Green Button pressed!")
    time.sleep(0.2)
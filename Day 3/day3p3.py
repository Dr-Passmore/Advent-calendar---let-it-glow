from machine import Pin
import time

redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

redlight = Pin(14, Pin.OUT)

while True:
    if redbutton.value() == 1:
        redlight.value(0)
    if greenButton.value() == 1:
        redlight.value(1)
    time.sleep(0.2)
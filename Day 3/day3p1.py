from machine import Pin
import time

redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)

while True:
    if redbutton.value() == 1:
        print("Button pressed!")
    time.sleep(0.2)
from machine import Pin
import time

redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
redlight = Pin(14, Pin.OUT)

while True:
    if redbutton.value() == 1:
        redlight.toggle()
    time.sleep(0.2)
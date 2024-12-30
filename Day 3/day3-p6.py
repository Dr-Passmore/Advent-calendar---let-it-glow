from machine import Pin
import time

greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)
redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)

redlight = Pin(14, Pin.OUT)

count = 0

while True:
    time.sleep(0.2)
    redlight.value(0)
    if redbutton.value() == 1:
        count -= 1
        redlight.value(1)
        print("Red Button pressed! Count:", count)
    if greenbutton.value() == 1:
        count += 1
        redlight.value(1)
        print("Green Button pressed! Count:", count)
from machine import Pin
import time

redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)

greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)

count = 0

while True:
    if redbutton.value() == 1:
        count -= 1
        print("Red Button pressed! Count:", count)
    if greenbutton.value() == 1:
        count += 1
        print("Green Button pressed! Count:", count)
    time.sleep(0.2)
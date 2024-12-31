from machine import Pin
import time

redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

segments = [seg1, seg2, seg3, seg4, seg5]

count = -1

for led in segments:
    led.value(0)

while True:
    if redbutton.value() == 1:
        if count == 4:
            pass
        else:
            count += 1
            segments[count].value(1)
            time.sleep(0.2)
    if greenButton.value() == 1:
        if count == -1:
            pass
        else:
            segments[count].value(0)
            count -= 1
            time.sleep(0.2)
           
from machine import Pin
import time

dip1 = Pin(6, Pin.IN, Pin.PULL_DOWN)
dip2 = Pin(5, Pin.IN, Pin.PULL_DOWN)
dip3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
dip4 = Pin(3, Pin.IN, Pin.PULL_DOWN)
dip5 = Pin(2, Pin.IN, Pin.PULL_DOWN)

seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

segments = [seg1, seg2, seg3, seg4, seg5]
dips = [dip1, dip2, dip3, dip4, dip5]

while True:
    for i in range(5):
        if dips[i].value() == 1:
            segments[i].value(1)
        else:
            segments[i].value(0)
    time.sleep(0.5)
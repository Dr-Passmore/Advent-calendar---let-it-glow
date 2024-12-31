from machine import Pin
import time
import random

seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

segments = [seg1, seg2, seg3, seg4, seg5]

while True:
    r = random.randint(0, 4)
    segments[r].value(1)
    time.sleep(0.1)
    segments[r].value(0)
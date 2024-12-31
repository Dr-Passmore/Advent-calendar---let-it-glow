from machine import Pin
import time

seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

segments = [seg1, seg2, seg3, seg4, seg5]

for led in segments:
    led.value(1)
    time.sleep(1)

for led in segments:
    led.value(0)
    time.sleep(1)
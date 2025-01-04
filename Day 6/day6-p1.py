import time
from machine import Pin
from neopixel import NeoPixel

GRBled = NeoPixel(Pin(2), 1)

GRBled.fill((0,0,255))

GRBled.write()
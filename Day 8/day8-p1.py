from machine import Pin
import time
from neopixel import NeoPixel

ring = NeoPixel(Pin(2), 12)

ring[0] = (10,0,0)

ring.write()

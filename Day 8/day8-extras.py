from machine import Pin
from neopixel import NeoPixel
import time
import random

ring = NeoPixel(Pin(2), 12)

ring.fill((0, 0, 0))
ring.write()
time.sleep(1)

while True:
    
    r = random.randint(0, 50)
    g = random.randint(0, 50)
    b = random.randint(0, 50)
    for i in range(12):
        ring[i] = (r, g, b)
    
        ring.write()

        time.sleep(0.05)
    for i in reversed(range(12)):
        ring[i] = (b, g, r)
        ring.write()
        time.sleep(0.05)

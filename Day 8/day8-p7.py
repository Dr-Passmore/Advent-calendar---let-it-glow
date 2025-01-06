from machine import Pin
from neopixel import NeoPixel
import time
import random

ring = NeoPixel(Pin(2), 12)

ring.fill((0, 0, 0))
ring.write()
time.sleep(1)

while True:
    randomled = random.randint(0, 11)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    ring[randomled] = (r, g, b)
    ring.write()

    time.sleep(0.05)

    ring.fill((0, 0, 0))   
    ring.write()
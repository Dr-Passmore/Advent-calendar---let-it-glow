from machine import Pin
from neopixel import NeoPixel
import time

ring = NeoPixel(Pin(2), 12)

myleds = [0, 3, 6, 9]

ring.fill((0, 0, 0))

ring.write()

time.sleep(1)

for i in myleds:
    ring[i] = (0, 0, 10)
    ring.write()
    time.sleep(1)
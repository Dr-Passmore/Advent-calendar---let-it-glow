import random
from machine import Pin, ADC
from neopixel import NeoPixel
import time

potentiometer = ADC(Pin(28))

GRBled = NeoPixel(Pin(2),1)
GRBled2 = NeoPixel(Pin(5), 1)

flash = 0

while True:
    flash = potentiometer.read_u16()/65535

    g = random.randint(0, 255)
    r = random.randint(0, 255)
    b = random.randint(0, 255)

    GRBled.fill((g, r, b))
    GRBled2.fill((g, r, b))
    GRBled.write()
    GRBled2.write()

    time.sleep(flash)
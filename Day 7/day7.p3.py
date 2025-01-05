import time
from machine import Pin, ADC
from neopixel import NeoPixel

potentiometer = ADC(Pin(28))

GRBled = NeoPixel(Pin(2),1)
GRBled2 = NeoPixel(Pin(5), 1)

analogureading = 0

GRBvalue = 0

while True:

    analogureading = potentiometer.read_u16()

    GRBvalue = round(analogureading * (255/65535))

    print("Analog Reading: ", analogureading)
    print("GRB Value: ", GRBvalue)

    GRBled.fill((0, 0, GRBvalue))
    GRBled2.fill((0, 0, GRBvalue))
    GRBled.write()
    GRBled2.write()

    time.sleep(0.1)
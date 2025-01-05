import time
from machine import Pin, ADC
from neopixel import NeoPixel

potentiometer = ADC(Pin(28))

GRBled = NeoPixel(Pin(2),1)

red = 0, 255, 0
amber = 255, 175, 150
green = 255, 0, 0

reading = 0

while True:
    reading = potentiometer.read_u16()
    print(reading)
    time.sleep(0.1)
    if reading <= 20000:
        GRBled.fill(red)
    elif 20000 < reading < 40000:
        GRBled.fill(amber)
    else:
        GRBled.fill(green)
    GRBled.write()
    
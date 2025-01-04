import time
from machine import Pin
from neopixel import NeoPixel

GRBled = NeoPixel(Pin(2), 1)

white = 240,140,255
red = 0,255,0
green = 255,0,0
blue = 0,0,255
yellow = 255,175,150
orange = 238,223,105
pink = 150,150,200
purple = 40,100,255
iceblue = 150,25,200
unicorn = 175,150,255
bogey = 215,100,0

colours = [white, red, green, blue, yellow, orange, pink, purple, iceblue, unicorn, bogey]

while True:
    for colour in colours:

        GRBled.fill((colour))

        GRBled.write()

        time.sleep(.5)
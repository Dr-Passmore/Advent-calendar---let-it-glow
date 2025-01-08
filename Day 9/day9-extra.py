from machine import Pin, I2C
import time
from dht20 import DHT20
from neopixel import NeoPixel

i2cl_sda = Pin(14)
i2cl_scl = Pin(15)
i2cl = I2C(1, sda=i2cl_sda, scl=i2cl_scl)
dht20 = DHT20(0x38, i2cl)

ring = NeoPixel(Pin(2), 12)

LEDdict = {
    14: 0,
    15: 1,
    16: 2,
    17: 3,
    18: 4,
    19: 5,
    20: 6,
    21: 7,
    22: 8,
    23: 9,
    24: 10,
    25: 11
}

white = 140,240,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 175,255,150
orange = 223,238,105
pink = 150,150,200
purple = 100,40,255
iceblue = 25,150,200
unicorn = 150,175,255
bogey = 100,215,0

while True:
    measurements = dht20.measurements

    temp = round(measurements['t'])

    if temp not in LEDdict:
        pass
    
    else:
        LEDindex = LEDdict[temp]

        print("Temperature: ", temp)
        print("LED Index: ", LEDindex)
        print("------------------------") # Divider
        ring.fill((0, 0, 0))
        ring.write()
        if temp > 23:
            ring[LEDindex] = red
        elif temp > 21 and temp < 23:
            ring[LEDindex] = orange
        elif temp > 19 and temp < 21:
            ring[LEDindex] = yellow
        elif temp > 17 and temp < 19: 
            ring[LEDindex] = green
        elif temp > 15 and temp < 17:
            ring[LEDindex] = blue
        else:
            ring[LEDindex] = iceblue
        ring.write()

    time.sleep(2)
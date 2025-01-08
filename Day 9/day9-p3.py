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

        ring[LEDindex] = (0, 100, 0)
        ring.write()

    time.sleep(2)
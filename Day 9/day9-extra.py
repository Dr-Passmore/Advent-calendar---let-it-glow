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


LEDcolours = [
    (0, 0, 50),  # Dark blue
    (5, 5, 50), # Medium blue
    (10, 10, 50), # Light blue
    (20, 20, 50), # Bright blue
    (25, 25, 50), # blueish
    (10, 50, 10), # Dark green
    (0, 50, 0),  # pure green
    (40, 50, 0), # yellowish
    (50, 20, 20), # Dark red
    (50, 10, 10), # Bright red
    (50, 2, 2), # Vibrant red
    (50, 0, 0),   # Solid bright red
]



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
            ring[LEDindex] = LEDcolours[11]
        elif temp > 21 and temp < 23:
            ring[LEDindex] = LEDcolours[9]
        elif temp > 19 and temp < 21:
            ring[LEDindex] = LEDcolours[7]
        elif temp > 17 and temp < 19: 
            ring[LEDindex] = LEDcolours[6]
        elif temp > 15 and temp < 17:
            ring[LEDindex] = LEDcolours[4]
        else:
            ring[LEDindex] = LEDcolours[3]
        ring.write()

    time.sleep(2)
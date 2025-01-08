from machine import Pin, I2C
import time
from dht20 import DHT20

i2cl_sda = Pin(14)
i2cl_scl = Pin(15)

i2cl = I2C(1, sda=i2cl_sda, scl=i2cl_scl)
dht20 = DHT20(0x38, i2cl)

while True:
    measurements = dht20.measurements

    print("-- Environment ---------") # Heading
    print(f"Temperature:      {round(measurements['t'],1)}°C")
    print(f"Humidity:         {round(measurements['rh'],1)}%")
    print("------------------------") # Divider
    print("                        ") # Empty line
    
    # Wait 5 seconds
    time.sleep(5)
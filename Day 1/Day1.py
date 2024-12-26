from machine import Pin
import time

while True:
        
    onboardLED= Pin(25, Pin.OUT)
    onboardLED.value(1)

    print("light on")

    time.sleep(2)
    
    onboardLED= Pin(25, Pin.OUT)
    onboardLED.value(0)
    
    print("light off")
    time.sleep(2)
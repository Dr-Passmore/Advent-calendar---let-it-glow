from machine import Pin
green = Pin(25, Pin.OUT)
blockLED = Pin(14, Pin.OUT)

blockLED.value(1)
green.value(1)

print("Both LEDs on!")

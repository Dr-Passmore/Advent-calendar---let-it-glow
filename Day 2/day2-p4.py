from machine import Pin
import time

# Create a Pin object for the red LED
red = Pin(14, Pin.OUT)

# Loop forever
while True:
    # Turn the red LED on
    red.value(1)
    # Wait for half a second
    time.sleep(0.5)
    # Turn the red LED off
    red.value(0)
    # Wait for half a second
    time.sleep(0.5)


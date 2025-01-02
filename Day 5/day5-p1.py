from machine import Pin
import time

dip1 = Pin(6, Pin.IN, Pin.PULL_DOWN)
dip2 = Pin(5, Pin.IN, Pin.PULL_DOWN)
dip3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
dip4 = Pin(3, Pin.IN, Pin.PULL_DOWN)
dip5 = Pin(2, Pin.IN, Pin.PULL_DOWN)

while True:
    if dip1.value() == 1:
        print("Switch 1 is on")
    if dip2.value() == 1:
        print("Switch 2 is on")
    if dip3.value() == 1:
        print("Switch 3 is on")
    if dip4.value() == 1:
        print("Switch 4 is on")
    if dip5.value() == 1:
        print("Switch 5 is on")

    print("-----------------")

    time.sleep(5)

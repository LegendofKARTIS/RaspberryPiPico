from machine import Pin
import time

ir_sensor = Pin(16, Pin.IN)

while True:
    if it_sensor.value() == 0:
        print("Object Detected!")
    else:
        print("No Object Detected")
        
    time.sleep(0.5)

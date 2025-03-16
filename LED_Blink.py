# Check out this Tutorial video on my channel: https://youtu.be/08o1DQNwnBU 
from machine import Pin
import utime
# Define the Onboard LED (GP25)
led = Pin(25, Pin.OUT)

while True:
  led.value(1)
  utime.sleep(1)
  led.value(0)
  utime.sleep(1)

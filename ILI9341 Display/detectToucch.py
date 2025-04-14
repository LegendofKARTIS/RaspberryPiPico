from machine import Pin, SPI
import xpt2046
import time

# Initialize SPI1 for the touchscreen
spi_touch = SPI(1, baudrate=1000000, polarity=0, phase=0,
                sck=Pin(10), mosi=Pin(11), miso=Pin(8))

# Initialize XPT2046 touch controller
touch = xpt2046.XPT2046(spi_touch, cs=9, irq=12, width=320, height=240, rotation=0)

# Test loop
while True:
    touch_data = touch.get_touch()
    if touch_data:
        print("Touch detected at:", touch_data)
    time.sleep(0.1)

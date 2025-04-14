from machine import Pin, SPI
import ili934xnew
import xpt2046
import time

# **Initialize SPI for Display (ILI9341)**
spi_display = SPI(0, baudrate=40000000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
display = ili934xnew.ILI9341(spi_display, cs=Pin(17), dc=Pin(15), rst=Pin(14), w=320, h=240, r=3)
display.init()

# **Clear screen manually (BLACK Background)**
BLACK = ili934xnew.color565(0, 0, 0)   # True black
WHITE = ili934xnew.color565(255, 255, 255)  # True white
display.fill_rectangle(0, 0, 320, 240, BLACK)  # Fill screen with black

# **Initialize SPI for Touch (XPT2046)**
spi_touch = SPI(1, baudrate=1000000, polarity=0, phase=0, sck=Pin(10), mosi=Pin(11), miso=Pin(8))
touch = xpt2046.XPT2046(spi_touch, cs=Pin(9), irq=Pin(12), width=320, height=240, rotation=0)  # Adjust rotation

# **Touchscreen Drawing Function**
def draw():
    while True:
        touch_data = touch.get_touch()

        if touch_data:
            x, y = touch_data
            
            # **Swap X and Y**
            x, y = y, x  # Swap coordinates

            # **Scale raw touch values to screen resolution**
            x = int((x / 4095) * 320)  # Normalize X
            y = int((y / 4095) * 240)  # Normalize Y


            print(f"Fixed Touch Data → X: {x}, Y: {y}")

            # **Draw White Dot**
            display.fill_rectangle(x, y, 4, 4, WHITE)  # White dot
        
        time.sleep(0.01)  # Short delay



# **Start Drawing**
draw()

from machine import Pin, SPI
import ili934xnew
import tt32

# SPI setup
spi = SPI(0, baudrate=40000000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))

# Initialize Display
display = ili934xnew.ILI9341(spi, cs=Pin(17), dc=Pin(15), rst=Pin(14), w=320, h=240, r=3)

# Initialize display
display.init()

# Define colors
BLACK = ili934xnew.color565(0, 0, 0)
WHITE = ili934xnew.color565(255, 255, 255)
RED = ili934xnew.color565(255, 0, 0)
BLUE = ili934xnew.color565(0, 0, 255)

# Fill screen with RED
display.fill_rectangle(10, 10, 300, 220, RED)
display.set_font(tt32)  # Large Font (Options: FONT_8X8, FONT_8X16, FONT_16X32)

# Display Text at the Center
display.set_pos(80, 100)  # Adjust position
display.set_color(WHITE, RED)  # Text: White, Background: Black
display.print("Subscribe panunga le !")


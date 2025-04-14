from machine import Pin, SPI
import ili934xnew

spi = SPI(0, baudrate=40000000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))

display = ili934xnew.ILI9341(spi, cs=Pin(17), dc=Pin(15), rst=Pin(14), w=320, h=240, r=3)
display.init()


def display_image(filename):
    with open(filename, "rb") as f:
        for y in range(240):  # Height of the image
            for x in range(320):  # Width of the image
                pixel_data = f.read(2)
                if not pixel_data:
                    break
                color = int.from_bytes(pixel_data, "big")
                display.pixel(x, y, color)

display_image("logo.rgb")
print("Done")

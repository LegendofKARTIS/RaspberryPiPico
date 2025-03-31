from machine import Pin, SPI
import time

class XPT2046:
    def __init__(self, spi, cs, irq=None, width=320, height=240, rotation=0):
        self.spi = spi
        self.cs = Pin(cs, Pin.OUT)
        self.irq = Pin(irq, Pin.IN, Pin.PULL_UP) if irq is not None else None
        self.width = width
        self.height = height
        self.rotation = rotation

    def read_raw(self, command):
        self.cs.value(0)
        self.spi.write(bytearray([command]))
        raw = self.spi.read(2)
        self.cs.value(1)
        return (raw[0] << 8 | raw[1]) >> 3  # Convert 12-bit data

    def get_touch(self):
        if self.irq and self.irq.value() == 1:
            return None  # No touch detected

        x = self.read_raw(0xD0)  # X position command
        y = self.read_raw(0x90)  # Y position command

        # Apply screen rotation if needed
        if self.rotation == 1:
            x, y = y, self.width - x
        elif self.rotation == 2:
            x, y = self.width - x, self.height - y
        elif self.rotation == 3:
            x, y = self.height - y, x

        return x, y

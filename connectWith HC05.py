from machine import Pin, UART
import utime

# Initialize UART1 (HC-05 on GP4 TX, GP5 RX)
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# Built-in LED (onboard Pico LED)
LED = Pin(25, Pin.OUT)

while True:
    if uart.any():  # Check if data is available
        data = uart.read().decode('utf-8').strip()  # Decode and clean input
        print(f"Received: {data}")  # Print received data

        if data == '1':  # Turn LED ON
            LED.value(1)
            print("LED ON")

        elif data == '2':  # Turn LED OFF
            LED.value(0)
            print("LED OFF")

    utime.sleep(0.2)  # Small delay to avoid CPU overload

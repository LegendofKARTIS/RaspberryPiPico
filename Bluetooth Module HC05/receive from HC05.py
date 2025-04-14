from machine import UART, Pin

# Set up UART0 for HC-05 (TX=GP4, RX=GP5)
uart = UART(0, baudrate=9600, tx=Pin(4), rx=Pin(5))

print("Enter a message to send to your phone:")

while True:
    msg = input()  # Read from Thonny's serial monitor
    uart.write(msg + "\n")  # Send to phone via HC-05

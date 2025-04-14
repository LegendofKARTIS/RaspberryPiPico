from machine import Pin, time_pulse_us
import utime

# Define sensor pins
TRIG = Pin(14, Pin.OUT)  # Trigger pin on GP14
ECHO = Pin(15, Pin.IN)   # Echo pin on GP15 (logic level shifted)

def measure_distance():
    # Ensure TRIG is low before starting
    TRIG.low()
    utime.sleep_us(2)
    
    # Send a 10µs pulse to trigger the sensor
    TRIG.high()
    utime.sleep_us(10)
    TRIG.low()

    # Measure the duration of the echo pulse
    pulse_time = time_pulse_us(ECHO, 1, 30000)  # Timeout after 30ms (max ~5m range)

    # Convert pulse time to distance (Speed of sound = 343m/s)
    distance = (pulse_time * 0.0343) / 2  # Convert to cm

    return distance

# Main loop
while True:
    dist = measure_distance()
    print(f"Distance: {dist:.2f} cm")
    utime.sleep(1)  # Wait 1 second before next measurement


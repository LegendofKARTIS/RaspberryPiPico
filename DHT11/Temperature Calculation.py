import dht
import machine
import utime

# Define the DHT11 sensor pin
DHT_PIN = machine.Pin(14)  # Change to your preferred GPIO pin
sensor = dht.DHT11(DHT_PIN)

while True:
    try:
        sensor.measure()  # Trigger measurement
        temp = sensor.temperature()  # Get temperature (°C)
        hum = sensor.humidity()  # Get humidity (%)
        6
        print(f"Temperature: {temp}°C, Humidity: {hum}%")
    
    except OSError as e:
        print("Failed to read sensor")

    utime.sleep(2)  # Wait 2 seconds before the next reading


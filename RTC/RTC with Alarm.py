from machine import I2C, Pin, PWM
from urtc import DS1307
import time

buzzer = PWM(Pin(16))
# Global variables
AlarmSet = False
alhour = None
alminute = None

dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
i2c_rtc = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
rtc = DS1307(i2c_rtc)

def showTime():
    (year, month, date, day, hour, minute, second, _) = rtc.datetime()
    print(f"Time: {hour:02}:{minute:02}:{second:02}")
    print(f"Date: {date:02}/{month:02}/{year}")
    print(f"Day: {dayOfWeek[day]}")

def setAlarm(ALhour, ALminute):
    global alhour, alminute, AlarmSet
    alhour = ALhour
    alminute = ALminute
    AlarmSet = True
    print(f"Alarm set for {alhour:02}:{alminute:02}")

def resetAlarm():
    global alhour, alminute, AlarmSet
    alhour = None
    alminute = None
    AlarmSet = False
    print("Alarm reset.")

def checkAlarm():
    global AlarmSet
    if not AlarmSet:
        return

    (year, month, date, day, hour, minute, second, _) = rtc.datetime()

    if alhour == hour and alminute == minute:
        print("🔔 Alarm ringing! 🔔")
        trigger_alarm()


def trigger_alarm():
    print("🚨 BEEP! BEEP! Alarm Active! 🚨")
    buzzer.freq(1000)  # Beep at 1000Hz
    buzzer.duty_u16(30000)  # Set volume (0-65535)
    time.sleep(0.5)  # Beep duration

    buzzer.duty_u16(0)  # Silence
    time.sleep(0.5)  # Pause duration


setAlarm(7, 35)  # Set alarm for 14:30
while True:
    showTime()
    checkAlarm()
    time.sleep(1)

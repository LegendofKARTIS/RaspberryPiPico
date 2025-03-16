from machine import I2C, Pin
from urtc import DS1307
import utime


dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
i2c_rtc = I2C(0,scl = Pin(1),sda = Pin(0),freq = 400000)
rtc = DS1307(i2c_rtc)

while True:
    (year,month,date,day,hour,minute,second,p1)=rtc.datetime()
    print("Time: " + str(hour) + ":" + str(minute) + ":" + str(second))
    #print(str(hour) + ":" + str(minute) + ":" + str(second))
    print("Date: " + str(date) + "/" + str(month) + "/" + str(year))
    #print(str(date) + "/" + str(month) + "/" + str(year))
    print(dayOfWeek[day])
    utime.sleep(1)

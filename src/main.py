# RTC: DS1307
# i2c scan() ==> 104 ==> 0x68

#from machine import Pin, UART
#from time import sleep
#
#uart = UART(0, 115200)
#uart.init(115200, bits=8, parity=None, stop=1)
#
#while True:
#    uart.write('WYSTARTOWAL')
#    sleep(5)

##################################################
from machine import I2C, Pin
import ds1307

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
i2c.scan()
##################################################
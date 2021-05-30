# #  This is a template for boot file.
# from machine import UART, freq
# from time import sleep
# uart = UART(0, 115200)
# uart.init(115200, bits=8, parity=None, stop=1)
#
# current_freq = freq()
#
# uart.write('********************************')
# uart.write(current_freq)
# uart.write('********************************')
from machine import Pin, UART
from time import sleep

uart = UART(0, 115200)
uart.init(115200, bits=8, parity=None, stop=1)

sleep(2)
uart.write('WYSTARTOWAL')
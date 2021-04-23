from machine import Pin
from time import sleep

led_pin = Pin(2, Pin.OUT)


while True:
    led_pin.on()
    sleep(5)
    led_pin.off()
    sleep(2)

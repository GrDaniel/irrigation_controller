from machine import Pin


class WaterPump(object):

    def __init__(self, control_pin, name):
        self._control_pin = Pin(control_pin, Pin.OUT)
        self.name = name
        self._state = 'off'

    def on(self):
        self._control_pin.on()
        self._state = 'on'

    def off(self):
        self._control_pin.off()
        self._state = 'off'

    def get_pump_status(self):
        return f"The pump: f{self.name} is {self._state}"

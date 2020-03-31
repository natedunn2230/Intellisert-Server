import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

class Controller: 
    def __init__(self):
        self.power = 'off'

    def turn_on(self):
        GPIO.output(21, GPIO.HIGH)
        self.power = 'on'

    def turn_off(self):
        GPIO.output(21, GPIO.LOW)
        self.power = 'off'

    def get_state(self):
        return {'power': self.power}

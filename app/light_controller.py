import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)


def turn_on():
    GPIO.output(21, GPIO.HIGH)

def turn_off():
    GPIO.output(21, GPIO.LOW)


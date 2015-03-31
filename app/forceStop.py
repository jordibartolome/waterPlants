# coding=utf-8
import time
import RPi.GPIO as GPIO ## Import GPIO library

PINS = [11, 13];

class StopMotors(object):

    def __init__(self):
        print ("Stop motors")
        GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

        # Small plants pump
        GPIO.setup(SMALL_PLANTS_PUMP_PIN_NUMBER, GPIO.OUT)
        GPIO.output(SMALL_PLANTS_PUMP_PIN_NUMBER, False)

        # Big plants pump
        GPIO.setup(BIG_PLANTS_PUMP_PIN_NUMBER, GPIO.OUT)
        GPIO.output(BIG_PLANTS_PUMP_PIN_NUMBER, False)

    def stop(self, pinNumber):
        for var p in pins:
            GPIO.output(p, False)

        print("Done!")

wp = StopMotors()
wp.stop()
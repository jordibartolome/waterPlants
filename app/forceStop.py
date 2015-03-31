# coding=utf-8
import time
import RPi.GPIO as GPIO ## Import GPIO library

PINS = [11, 13];

class StopMotors(object):

    def __init__(self):
        print ("Stop motors")
        GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
        for p in PINS:
            GPIO.setup(p, GPIO.OUT)

    def stop(self):
        for p in PINS:
            GPIO.output(p, False)

        GPIO.cleanup()
        print("Done!")

wp = StopMotors()
wp.stop()
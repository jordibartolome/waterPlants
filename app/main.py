# coding=utf-8
import time
import RPi.GPIO as GPIO ## Import GPIO library

SMALL_PLANTS_PUMP_PIN_NUMBER = 11;
BIG_PLANTS_PUMP_PIN_NUMBER = 13;

SMALL_PLANTS_PUMP_SECONDS = 10;
BIG_PLANTS_PUMP_SECONDS = 15;

class WaterPlants(object):

    def __init__(self):
        print ("Initializing...")
        GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

        # Small plants pump
        GPIO.setup(SMALL_PLANTS_PUMP_PIN_NUMBER, GPIO.OUT)
        GPIO.output(SMALL_PLANTS_PUMP_PIN_NUMBER, False)

        # Big plants pump
        GPIO.setup(BIG_PLANTS_PUMP_PIN_NUMBER, GPIO.OUT)
        GPIO.output(BIG_PLANTS_PUMP_PIN_NUMBER, False)

    def startPump(self, pinNumber):
        GPIO.output(pinNumber, True)

    def stopPump(self, pinNumber):
        GPIO.output(pinNumber, False)

    def doWateringProcess(self, pinNumber, seconds):
        self.startPump(pinNumber)
        time.sleep(seconds)
        self.stopPump(pinNumber)

    def waterPlants(self):
        print("Watering plants...")
        # First pump
        print ('Pump small plants')
        self.doWateringProcess(SMALL_PLANTS_PUMP_PIN_NUMBER, SMALL_PLANTS_PUMP_SECONDS);

        print ('Pump big plants')
        # Second pump
        self.doWateringProcess(BIG_PLANTS_PUMP_PIN_NUMBER, BIG_PLANTS_PUMP_SECONDS);

        # Clean up
        GPIO.cleanup()
        print("Done!")

wp = WaterPlants()
wp.waterPlants()
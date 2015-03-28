# coding=utf-8
import time
import RPi.GPIO as GPIO ## Import GPIO library

FIRST_PUMP_PIN_NUMBER = 7;
SECOND_PUMP_PIN_NUMBER = 11;

FIRST_PUMP_SECONDS = 10;
SECOND_PUMP_SECONDS = 15;

class WaterPlants(object):

	def __init__(self):
		print ("Initializing...")
		initialize();

	def initialize():
		GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

		# First pump
		GPIO.setup(FIRST_PUMP_PIN_NUMBER, GPIO.OUT)
		GPIO.output(FIRST_PUMP_PIN_NUMBER, False)

		# Second pump
		GPIO.setup(SECOND_PUMP_PIN_NUMBER, GPIO.OUT)
		GPIO.output(SECOND_PUMP_PIN_NUMBER, False)

	def startPump(pinNumber):
		GPIO.output(pinNumber, True)

	def stopPump(pinNumber):
		GPIO.output(pinNumber, False)

	def doWateringProcess(pinNumber, seconds):
		self.startPump(pinNumber)
		time.sleep(seconds)
		self.stopPump(pinNumber)

	def waterPlants(self):
		print("Watering plants...")
		# First pump
		doWateringProcess(FIRST_PUMP_PIN_NUMBER, FIRST_PUMP_SECONDS);

		# Second pump
		doWateringProcess(SECOND_PUMP_PIN_NUMBER, SECOND_PUMP_SECONDS);

		# Clean up
		GPIO.cleanup()
		print("Done!")

wp = WaterPlants()
wp.waterPlants()
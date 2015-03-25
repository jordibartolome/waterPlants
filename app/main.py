# coding=utf-8
# import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO ## Import GPIO library

PIN_NUMBER = 7;

class WaterPlants(object):

	def __init__(self):
		print ("Initializing...")

	def start(self):
		print ("Start")
		GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
		GPIO.setup(PIN_NUMBER, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
		GPIO.output(PIN_NUMBER, True) ## Turn on GPIO pin 7
		print GPIO.input(PIN_NUMBER)

	def stop(self):
		print ("Stop")
		GPIO.output(PIN_NUMBER, False) ## Turn on GPIO pin 7
		GPIO.cleanup()

	def waterPlants(self):
		print("Watering plants...")
		self.start()
		time.sleep(10)
		self.stop()
		print("Done!")

wp = WaterPlants()
wp.waterPlants()



# GPIO.setmode(GPIO.BCM)

# GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# while True:

# 	GPIO.wait_for_edge(23, GPIO.RISING)

# 	print(“Button 1 Pressed”)

# 	GPIO.wait_for_edge(23, GPIO.FALLING)

# 	print(“Button 1 Released”)

# 	GPIO.wait_for_edge(24, GPIO.FALLING)

# 	print(“Button 2 Pressed”)

# 	GPIO.wait_for_edge(24, GPIO.RISING)

# 	print(“Button 2 Released”)

# GPIO.cleanup()

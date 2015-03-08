# coding=utf-8
# import RPi.GPIO as GPIO
import time

class WaterPlants(object):

	def __init__(self):
		print ("Initializing...")

	def start(self):
		print ("Start")

	def stop(self):
		print ("Stop")

	def waterPlants(self):
		print("Watering plants...")
		self.start()
		time.sleep(3)
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

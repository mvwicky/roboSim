import os
import sys
import random
import math

class servo(object):
	"""Generic Servo Object"""
	def __init__(self,port,position=0,sprite=None):
		self.port=port
		self.position=position
		self.enabled=False
		self.sprite=sprite


	def draw(self):
		pass

	def setPosition(self,position):
		pass
	def moveToPosition(self,position,step):
		pass

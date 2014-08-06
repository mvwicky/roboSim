import os
import sys
import random
import math

class motor(object):
	"""Generic motor object"""
	def __init__(self,port,wheelRad,ticks,tolerance=0):
		self.port=port
		self.positon=0
		self.wheelRad=wheelRad
		self.tolerance=tolerance

	def moveAtVelocity(self,velocity):
		pass
	
	def moveRelativePosition(self,velocity,position):
		pass
	
	def moveToPosition(self,velocity,position):
		pass

	def getPosition(self):
		pass

	def forward(self):
		pass

	def off(self):
		pass

	def zeroMotor(self):
		pass
	
	def mav(self,velocity):
		pass
	def mrp(self,velocity,position):
		pass
	def mtp(self,velocity,position):
		pass
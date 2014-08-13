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
		self.ticks=ticks
		#self.distPerTick
		#self.sprite
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
	"""Sets themotor position back to zero"""
		pass

	def getPosition(self):
	"""Returns the motor position"""
		pass
	
	def mav(self,velocity):
		return self.moveAtVelocity(velocity)
	def mrp(self,velocity,position):
		return self.moveRelativePosition(velocity,position)
	def mtp(self,velocity,position):
		return self.moveToPosition(velocity,position)
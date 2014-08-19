import os
import sys
import random
import math

import utilFunctions as utlF

class motor(object):
	"""Generic motor object"""
	def __init__(self,port,wheelRad=0,ticks=1000,tolerance=0,sprite=None):
		"""port:which port the motor is in
		   wheelRad:the radius of the attached wheel
		      if not a drive motor: wheelRad=0
		   ticks:number of ticks per revolution
		   tolerance:
		   sprite:path to the sprite
		"""
		self.port=port
		self.positon=0
		self.wheelRad=wheelRad
		self.ticks=ticks
		self.lastSpeed=0
		self.currentSpeed=0
		#self.distPerTick
		self.context=None
		if sprite==None:
			pass
		elif sprite!=None and type(sprite)!=utlF.sprite:
			print("Invalid sprite")
		elif sprite!=None and type(sprite)==utlF.sprite:
			self.sprite=sprite 
		self.tolerance=tolerance

	def update(self):
		if self.context==None:
			print("Context not defined")
			return -1
		else:
			pass

	def draw(self):
		pass

	def moveAtVelocity(self,velocity):
		self.currentSpeed=velocity
		return 0
	
	def moveRelativePosition(self,velocity,delta):
		pass
	
	def moveToPosition(self,velocity,position):
		pass

	def moveAngleDeg(self,velocity,theta):
		pass

	def moveAngleRad(self,velocity,theta):
		pass

	def getPosition(self):
		pass

	def forward(self):
		pass

	def off(self):
		pass

	def zeroMotor(self):
		"""Sets the motor position back to zero"""
		pass
	
	def mav(self,velocity):
		return self.moveAtVelocity(velocity)
	def mrp(self,velocity,position):
		return self.moveRelativePosition(velocity,position)
	def mtp(self,velocity,position):
		return self.moveToPosition(velocity,position)
	def mad(self,velocity,theta):
		return self.moveAngleDeg(velocity,theta)
	def mar(self,velocity,theta):
		return self.moveAngleRad(velocity,theta)
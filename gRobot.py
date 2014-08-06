import sfml
import os
import sys
import random
import math

from utilFunctions import *
from gSensors import *

class robot(object):
	"""Basically a generic robot"""
	def __init__(self,dMotors=None,gMotors=None,servos=None,aSensors=None,dSensors=None):
	# These inputs should be arrays of objects
	# 	dSensors: digital sensors
	# 	dMotors: drive motors
	# 	gMotors: other motors
	# 	servos: servos
	# 	aSensors: analog sensors
		self.servosEnabled=False
		
		if dMotors==None:
			pass
		elif dMotors!=None:
			pass

		if gMotors==None:
			pass
		elif gMotors!=None:
			pass

		if servos==None:
			pass
		elif servos!=None:
			pass

		if aSensors==None:
			pass
		elif aSensors!=None:
			pass

		if dSensors==None:
			pass
		elif dSensors!=None:
			pass

		self.configuration=[]

	def analog(self,sensId):
	"""Returns an analog value
	   Args: """
		pass
	
	def digtal(self,sensId):
	"""Returns a digital value (0 or 1)
	   Args: """
		pass
	
	def digitalBool(self,sensId):
	"""Returns a digital value as a boolean
	   Args: """
		pass
	
	def enableServos(self):
		pass
	
	def disableServos(self):
		pass
	
	def msleep(self):
		pass
	
	def driveDistance(self,velocity,distance):
		pass



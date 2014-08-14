import sfml
import os
import sys
import random
import math

from utilFunctions import *

from gSensors import *
from motors import *
from servos import *

class robot(object):
	"""Basically a generic robot"""
	def __init__(self,numMPorts,numSPorts=None,numAPorts=None,numDPorts=None):
		"""numMPorts:the number of motor ports
		   numSPorts:the number of servo ports
		   numAPorts:the number of analog ports
	 	   numDPorts:the number of digital ports
		   -one or four inputs can be given:
				one given: is an array->[mPorts,sPorts,aPorts,dPorts]
				four given: just four numbers
		"""

		if vecCheck(numMPorts) and numSPorts==None and numAPorts==None and numDPorts==None:
			self.config=numMPorts
		elif numSPorts!=None and numAPorts!=None and numDPorts!=None:
			self.config=[numMPorts,numSPorts,numAPorts,numDPorts]
		else:
			print("invalid input(s)")
			return None

		self.servosEnabled=False
		self.dMotors=[] # array to store the drive motors
		self.gMotors=[] # array to store other motors
		self.servos=[] # array to store servos
		self.aSensors=[]  # array to store analog sensors
		self.dSensors=[] # array to store digital sensors

	def draw(self):
		pass

	def addDriveMotors(self,lMot,rMot):
		pass

	def addMotor(self,mot):
		pass

	def addServo(self,servo):
		pass

	def addAnalogSensor(self,sens):
		pass

	def addDigitalSensor(self,sens):
		pass

	def analog(self,sensId):
		try:
			sensId.sample()
		except NameError:
			print ("Not a valid sensor")
			return -1
		return sensId.sample()
	
	def digtal(self,sensId):
		try:
			sensId.sample()
		except NameError:
			print ("Not a valid sensor")
			return -1
		return sensId.sample()
	
	def digitalBool(self,sensId):
		try: 
			sensId.sample()
		except NameError:
			print ("Not a valid sensor")
			return -1
		if sensId.sample()==1:
			return True
		elif sensId.sample()==0:
			return False
		else:
			print("Problem with sensor")
			return False
		pass
	
	def enableServos(self):
		pass
	
	def disableServos(self):
		pass
	
	def msleep(self,msec):
		pass
	
	def driveDistance(self,velocity,distance):
		pass

	def writeToScreen(self,text,pVec):
		pass





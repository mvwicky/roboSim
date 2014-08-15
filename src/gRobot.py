import sfml
import os
import sys
import random
import math

from utilFunctions import *

#from gSensors import *
#from motors import *
#from servos import *

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
			self.config=tuple(numMPorts)
		elif numSPorts!=None and numAPorts!=None and numDPorts!=None:
			self.config=(numMPorts,numSPorts,numAPorts,numDPorts)
		else:
			print("invalid input(s)")
			return None

		self.servosEnabled=False
		self.dMotors=[] # array to store the drive motors
		self.gMotors=[] # array to store other motors
		self.servos=[] # array to store servos
		self.aSensors=[]  # array to store analog sensors
		self.dSensors=[] # array to store digital sensors

	def update(self):
		pass

	def draw(self):
		pass

	def addDriveMotors(self,lMot,rMot,dist):
		pass

	def addMotor(self,mot):
		if len(self.gMotors)+len(self.dMotors)<self.config[0]+1:
			print("Not enough motor ports")
			return -1
		else:
			self.gMotors.append(mot)

	def addServo(self,servo):
		if servo.port not in range(self.config[1]):
			print("Port not in range")
			return -1
		for i in range(len(self.servos)):
			if servo.port==self.servos[i].port:
				print("Port already used")
				return -1
		if len(self.servos)>=self.config[1]:
			print("Not enough servo ports")
			return -1
		else:
			self.servos.append(servo)

	def addAnalogSensor(self,sens):
		if len(self.aSensors)<self.config[2]+1:
			print("Not enough analog sensor ports")
			return -1
		else:
			self.aSensors.append(sens)

	def addDigitalSensor(self,sens):
		if len(self.dSensors)<self.config[3]+1:
			print("Not enough digital sensor ports")
			return -1
		else:
			self.dSensors.append(sens)

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
 	def enableServo(self,servo):
		if servo in self.servos:
			self.servos[self.servos.index(servo)].enabled=True
		else:
			print("servo name not recognized")
	def enableServos(self):
		for i in range(len(self.servos)):
			self.servos[i].enabled=True
		return 0
	
	def disableServos(self):
		for i in range(len(self.servos)):
			self.servos[i].enabled=False
		return 0
	
	def msleep(self,msec):
		pass
	
	def driveDistance(self,velocity,distance):
		pass

	def writeToScreen(self,text,pVec):
		pass





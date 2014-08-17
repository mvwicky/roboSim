import sfml
import os
import sys
import random
import math

from utilFunctions import *

from gSensors import analogSensor,digitalSensor
from motors import motor
from servos import servo

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
		if type(mot)!=motor:
			print("Invalid Argument")
			return -1
		if mot.port not in range(self.config[0]):
			print("Port not in range")
			return -1
		bMot=self.dMotors+self.gMotors
		for i in bMot:
			if mot.port==i.port:
				print("Port already used")
				return -1
		if len(self.gMotors)+len(self.dMotors)>=self.config[0]:
			print("Not enough motor ports")
			return -1
		else:
			self.gMotors.append(mot)

	def addServo(self,ser):
		if type(ser)!=servo:
			print("Invalid Argument")
			return -1
		if ser.port not in range(self.config[1]):
			print("Port not in range")
			return -1
		for i in self.servos:
			if ser.port==i.port:
				print("Port already used")
				return -1
		if len(self.servos)>=self.config[1]:
			print("Not enough servo ports")
			return -1
		else:
			self.servos.append(ser)

	def addAnalogSensor(self,sens):
		if type(sens)!=analogSensor:
			print("Invalid Argument")
			return -1
		if sens.port not in range(self.config[2]):
			print("Port not in range")
			return -1
		for i in self.aSensors:
			if sens.port==i.port:
				print('Port already used')
				return -1
		if len(self.aSensors)>=self.config[2]:
			print("Not enough analog sensor ports")
			return -1
		else:
			self.aSensors.append(sens)

	def addDigitalSensor(self,sens):
		if type(sens)!=digitalSensor:
			print("Invalid Argument")
			return -1
		if sens.port not in range(self.config[3]):
			print("Port not in range")
			return -1
		for i in self.dSensors:
			if sens.port==i.port:
				print("Port already used")
				return -1
		if len(self.dSensors)>=self.config[3]:
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

	def setServoPosition(self,servo,position):
		pass

	def moveServoToPosition(self,servo,position,step):
		pass
	
	def msleep(self,msec):
		pass
	
	def driveDistance(self,velocity,distance):
		pass

	def writeToScreen(self,text,pVec):
		pass





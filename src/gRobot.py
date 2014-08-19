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
	def __init__(self,numMPorts,numSPorts=None,numAPorts=None,numDPorts=None,context=None):
		"""context: the scene that the bot lives in
		   numMPorts:the number of motor ports
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
			print("Invalid input(s)")
			return None

		self.servosEnabled=False

		self.dMotors=dict() # dict to store the drive motors (and the distance between them)
		self.gMotors=[] # array to store other motors
		self.servos=[] # array to store servos
		self.aSensors=[]  # array to store analog sensors
		self.dSensors=[] # array to store digital sensors

		self.context=None

	def defineContext(self,context):
		"""context: scene that the bot lives in"""
		self.context=context
		if self.dMotors!={}:
			self.dMotors["left"].context=context
			self.dMotors["right"].context=context
		for i in range(len(self.gMotors)):
			self.gMotors[i].context=context
		for i in range(len(self.servos)):
			self.servos[i].context=context
		for i in range(len(self.aSensors)):
			self.aSensors[i].context=context
		for i in range(len(self.dSensors)):
			self.dSensors[i].context=context
		return 0

	def update(self):
		if self.dMotors!={}:
			self.dMotors["left"].update()
			self.dMotors["right"].update()
		for i in range(len(self.gMotors)):
			self.gMotors[i].update()
		for i in range(len(self.servos)):
			self.servos[i].update()
		for i in range(len(self.aSensors)):
			self.aSensors[i].update()
		for i in range(len(self.dSensors)):
			self.dSensors[i].update()
		return 0

	def draw(self):
		pass

	def addDriveMotors(self,lMot,rMot,dist):
		"""left motor object
		   right motor object
		   distance between motors(mm)"""
		if type(lMot)!=motor or type(rMot)!=motor or not numCheck(dist):
			print("Invalid Arguments")
			return -1
		if lMot.port not in range(self.config[0]) or rMot.port not in range(self.config[0]):
			print("Port(s) not in range")
			return -1
		for i in self.gMotors:
			if lMot.port==i.port or rMot.port==i.port:
				print("Port(s) already used")
				return -1
		if lMot.port==rMot.port:
			print("Motors have the same port")
			return -1
		if len(self.dMotors)+len(self.gMotors)>=self.config[0]:
			print("Not enough motor ports")
			return -1
		else:
			self.dMotors["left"]=lMot
			self.dMotors["right"]=rMot
			self.dMotors["dist"]=dist



	def addMotor(self,mot):
		if type(mot)!=motor:
			print("Invalid Argument")
			return -1
		if mot.port not in range(self.config[0]):
			print("Port not in range")
			return -1
		for i in self.gMotors:
			if mot.port==i.port:
				print("Port already used")
				return -1
		if self.dMotors!={}:
			if self.dMotors["left"].port==mot.port:
				print("Port already used")
				return -1
			if self.dMotors["right"].port==mot.port:
				print("Port already used")
				return -1
		if len(self.dMotors)+len(self.gMotors)>=self.config[0]:
			print("Not enough motor ports")
			return -1
		else:
			self.gMotors.append(mot)
			return 0

	def addMotors(self,*mots):
		for i in range(len(mots)):
			self.addMotor(mots[i])
		return 0

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
			return 0

	def addServos(self,*sers):
		for i in range(len(sers)):
			self.addServo(sers[i])
		return 0

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





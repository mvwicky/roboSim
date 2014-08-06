import sfml
import os
import sys
import random
import math

from utilFunctions import *

from gSensors import *
from motors import *
from servos import *
from interface import *

class robot(object):
	"""Basically a generic robot"""
	def __init__(self,dMotors=None,gMotors=None,servos=None,aSensors=None,dSensors=None):
	# INPUTS:
	# 	dMotors: drive motors
	#		should be two motor objects (left,right) followed by their distance apart (mm)
	# 	gMotors: other motors
	#		just an array of motor objects
	# 	servos: servos
	#		array of servo objects
	# 	aSensors: analog sensors
	# 	dSensors: digital sensors
		self.servosEnabled=False
		self.dMotors=[]
		self.gMotors=[]
		self.servos=[]
		self.aSensors=[]
		self.dSensors=[]

		self.screen
		
		if dMotors==None or len(dMotors)!=3:
			print("Drive Motors not inputted correctly")
		elif dMotors!=None:
			self.dMotors.append(dMotors[0]) # left motor object
			self.dMotors.append(dMotors[1]) # right motor object
			self.dMotors.append(dMotors[2]) # distance apart

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

		self.driveTrain=dict()
		self.driveTrain={"leftMotor":self.dMotors[0],
							"rightMotor":self.dMotors[1],
							"distApart":self.dMotors[2]}

	def drawBot(self):
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
	
	def msleep(self):
		pass
	
	def driveDistance(self,velocity,distance):
		pass

	def writeToScreen(self,text,pVec):
		pass





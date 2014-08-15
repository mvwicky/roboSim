import os
import sys
import random
import math

from time import sleep

class servo(object):
	"""Generic Servo Object"""
	def __init__(self,port,position=0,sprite=None):
		self.port=port
		self.position=position
		self.enabled=False
		self.sprite=sprite

	def update(self):
		pass

	def draw(self):
		pass

	def setPosition(self,position):
		self.position=position
		return 0

	def moveToPosition(self,pos,step):
		if self.pos>pos:
			while self.pos>pos:
				self.pos-=step
			return 0
		elif self.pos<pos:
			while self.pos<pos:
				self.pos+=step
		else:
			return 0

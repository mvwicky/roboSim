import os
import sys
import random
import math

class motor(object):
"""Generic motor object"""
	def __init__(self,port,tolerance=0):
		self.port=port
		self.tolerance=tolerance
	def moveAtVelocity(self,velocity):
		pass
	def moveRelativePosition(self,velocity,positon):
		pass
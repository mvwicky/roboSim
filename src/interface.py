import sfml
import os
import sys
import random
import math

from utilFunctions import *
import gRobot

class simScreen(sfml.RenderWindow):
	"""Class for the screen of the sim"""
	def __init__(self,width,height,title="Robo Sim",color=sfml.Color(100,100,200,255),icon=None):
		super(simScreen,self).__init__(sfml.VideoMode(width,height),title)
		self.framerate_limit=60
		self.color=color
		if icon!=None:
			self.icon=icon.pixels


class robotScreen():
	pass
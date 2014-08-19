import sfml
import os
import sys
import random
import math

from utilFunctions import *
import gRobot

class simScreen(sfml.RenderWindow):
	"""Class for the screen of the sim"""
	def __init__(self,width,height,title="Robo Sim",color=sfml.Color(100,100,200,255),icon=None,config=None):
		super(simScreen,self).__init__(sfml.VideoMode(width,height),title)
		self.framerate_limit=60
		self.color=color
		self.config=config
		if icon!=None:
			self.icon=icon.pixels



class robotScreen(object):
	"""Class for the screen of the robot"""
	def __init__(self,context=None):
		self.mainScreen=sfml.RectangleShape()
		self.buttons=dict()
		self.buttons['a']=sprite('../sprites/aButton.cfg')
		self.buttons['b']=sprite('../sprites/bButton.cfg')
		self.buttons['c']=sprite('../sprites/cButton.cfg')
		self.buttons['side']=sprite('../sprites/cButton.cfg')
		self.context=context
	def draw(self,window):
		pass
	def pressButton(self,button):
		pass
	def releaseButton(self,button):
		pass
	def clickButton(self,button):
		pass
	def checkIfPressed(self,pVec,button):
		pass
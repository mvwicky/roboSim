import sfml as sf
import sys
import os
import random
import math

from utilFunctions import *

#
# This particular program is basically a test for what will be the actual sim
#

class vector4(object): # contains two points (basically a line)
	def __init__(self, x0,y0,x1,y1):
		self.p0=sf.Vector2(x0,y0)
		self.p1=sf.Vector2(x1,y1)


class basicRobot(object): # a basic robot, a test
	def __init__(self,*args): 
		self.body=sf.RectangleShape()
		self.lWheel=sf.RectangleShape()
		self.rWheel=sf.RectangleShape()

		self.body.size=(50,100)
		self.lWheel.size=(24,24)
		self.rWheel.size=(24,24)

		self.body.origin=(25,50)
		self.lWheel.origin=(12,12)
		self.rWheel.origin=(12,12)

		self.body.fill_color=sf.Color.RED
		self.lWheel.fill_color=sf.Color.BLUE
		self.rWheel.fill_color=sf.Color.YELLOW

		self.body.outline_color=sf.Color.BLACK
		self.lWheel.outline_color=sf.Color.BLACK
		self.rWheel.outline_color=sf.Color.BLACK

		self.body.outline_thickness=1
		self.lWheel.outline_thickness=1
		self.rWheel.outline_thickness=1

		self.body.position=(250,250)
		self.lWheel.position=(214,250)
		self.rWheel.position=(286,250)
	def rotateBy(self,theta): 
		# basically the way that this works is that the distances from the origin 
		# of the center block to the origin of the outer blocks are treated as radii
		# then the new coordinates of the outer blocks are calculated as opposed to a 
		# straight rotation
		pass
	def translate(self,tVec):
		pass
	def 
	

def main():
	window=sf.RenderWindow(sf.VideoMode(500,500),"Robo Test")
	window.framerate_limit=60
	
	newBot=basicRobot()

	print("lWheel: ",newBot.lWheel.position)
	print("rWheel: ",newBot.rWheel.position)

	while window.is_open:
		window.clear(sf.Color.CYAN)

		window.draw(newBot.body)
		window.draw(newBot.lWheel)
		window.draw(newBot.rWheel)

		for event in window.events:
			 if type(event)==sf.CloseEvent:
			 	window.close()
			 if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
			 	newBot.body.rotate(-90)
			 	newBot.lWheel.move((-36,36))
			 	newBot.rWheel.move((36,-36))
			 if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
			 	newBot.body.rotate(90)
			 	newBot.lWheel.move((36,-36))
			 	newBot.rWheel.move((-36,36))
			 if sf.Keyboard.is_key_pressed(sf.Keyboard.RETURN):
			 	window.close()
		window.display()

if __name__=='__main__':
	main()
import os
import sys
import random

from math import pi,sqrt,atan

from sfml import Vector2,Vector3,Color,Image

from sfml import Sprite,Texture,Rectangle

class line(object):
	"""class for storing two points"""
	def __init__(self,x0,y0,x1=None,y1=None):
		if vecCheck(x0) and vecCheck(y0) and x1==None and y1==None:
		# two arguments: two points
			self.p0=x0
			self.p1=y0
		elif x1!=None and y1!=None:
		# fout arguments: four coordinates
			self.p0=[x0,y0]
			self.p1=[x1,y1]

class configs(object):
	"""class that stores configurations for various things
		basically an argument generator"""
	def __init__(self):
		self.link=(4,4,6,4)

class sprite(Sprite):
	"""class that will store the image of a sprite as well
	   as its bounding box and other info"""
	def __init__(self,cfg):
		"""cfg: path to config file for sprite"""
		try:
			c=open(cfg,'r')
		except IOError:
			print("File not found")
			return None
		cts=c.read()
		c.close()	
		try:
			self.path=str(cts[cts.index("p")+5:cts.index("endl1")-1])
			self.size=str(cts[cts.index("size")+5:cts.index("endl2")-1])
		except ValueError:
			print("Error with config file")
			return None
		try:
			self.image=Texture.from_file(self.path)
		except IOError:
			print("Could not load image")
			return None

		super(sprite,self).__init__(self.image)

		self.bounds=self.genBounds()
	
	def genBounds(self):
		pass


def clear():
# clears the console
	if sys.platform=='win32': # windows
		os.system('cls')
	elif sys.platform=='linux': # linux
		os.system('clear') 
	else:
		print("platform not recognized/supported")

def pause():
# pauses the console
	if sys.platform=='win32':
		os.system('pause')
	else:
		print("platfrom not recognized/supported")

def vecCheck(tVec): 
# checks if the input vector is in a range of default types
	if type(tVec) in (tuple,list,Vector2,Vector3):
		return True
	else:
		return False

def numCheck(num):
# checks if num is a number
	if type(num) in (int,float):
		return True
	else:
		return False

def typeCheck(input,types): # need to fix the case of having only one type
# basically checks if input is a member of 'types'
	if type(input) in types:
		return True
	else:
		return False

def retIndicies(iVec,ind):
# returns the selected indicies 
# input should be an array of arrays (test?)
	ret=[]
	for i in range(len(iVec)):
		ret.append(iVec[i][ind])
	return tuple(ret)

def inXPlane(yCoord,tL,bR):
	if vecCheck(tL) and vecCheck(bR):
		if (vCoord>=tL[1] and yCoord<=bR[1]):
			return True
		else:
			return False
	else:
		print("Invalid Argument(s)")
		return -1


def inYPlane(xCoord,tl,bR):
	if vecCheck(tL) and vecCheck(bR):
		if (xCoord>=tL[0] and xCoord<=bR[0]):
			return True
		else:
			return False
	else:
		print("Invalid Argument(s)")
		return -1

def touching(sPoint1,ePoint1,sPoint2=None,ePoint2=None):
	"""tests whether or not two lines are touching"""
	if type(sPoint1)==line and type(ePoint1)==line and sPoint2==None and ePoint2==None:
		pass
	elif vecCheck(sPoint1) and vecCheck(ePoint1) and vecCheck(sPoint2) and vecCheck(ePoint2):
		pass
	else:
		print("Invalid Argument(s)")
		return -1

def pointInLine(point,sPoint,ePoint=None):
	"""tests whether or not a point is touching a line"""
	pass

def pointIn(pVec,tL,bR):
	if vecCheck(pVec) and vecCheck(tL) and vecCheck(bR):
		if inXPlane(pVec[1],tL,bR) and inYPlane(pVec[0],tL,bR):
			return True
		else:
			return False
	else:
		print("Invalid Argument(s)")
		return -1

def degToRad(deg):
	rad=deg*(pi/180)
	return rad

def radToDeg(rad):
	deg=rad*(180/pi)
	return deg

def calcLength(sPoint,ePoint=None):
	if type(sPoint)==line and ePoint==None:
	# one argument: a line object
		return sqrt(((sPoint.p0[0]-sPoint.p1[0])**2)*((sPoint.p0[1]-sPoint.p1[1])**2))
	elif vecCheck(sPoint) and vecCheck(ePoint):
	# two arguemtns: two points
		return sqrt(((sPoint[0]-ePoint[0])**2)*((sPoint[1]-ePoint[1])**2))
	elif not vecCheck(sPoint) and not vecCheck(ePoint):
		print("Invalid Argument(s)")
		return -1

def calcSlope(sPoint,ePoint=None):
	if type(sPoint)==line and ePoint==None:
	# one argument: a line object
		return (sPoint.p0[1]-sPoint.p1[1])/(sPoint.p0[0]-sPoint.p1[0])
	elif vecCheck(sPoint) and vecCheck(ePoint):
	# two arguments: two points
		return (sPoint[1]-ePoint[1])/(sPoint[0]-ePoint[0])
	elif not vecCheck(sPoint) and not vecCheck(ePoint):
		print("Invalid Argument(s)")
		return -1

def calcAngleRad(sPoint1,ePoint1,sPoint2=None,ePoint2=None):
	if type(sPoint1)==line and type(ePoint1)==line and sPoint2==None and ePoint2==None:
		pass
	elif vecCheck(sPoint1) and vecCheck(ePoint1) and vecCheck(sPoint2) and vecCheck(ePoint2):
		pass
	else:
		print("Invalid Argument(s)")
		return -1

def calcAngleDeg(sPoint1,ePoint1,sPoint2=None,ePoint2=None):
	return radToDeg(calcAngleRad(sPoint1,ePoint1,sPoint2,ePoint2))
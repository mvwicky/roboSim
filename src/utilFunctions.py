import math
import os
import sys
import random

from sfml import Vector2
from sfml import Vector3
from sfml import Color

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
	elif not vecCheck(tL) or not vecCheck(bR):
		print("Type(s) are wrong")
		return False


def inYPlane(xCoord,tl,bR):
	pass

def inZPlane():
	pass

def pointIn(pVec,tL,bR):
	pass

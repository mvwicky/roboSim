import sfml as sf
import sys
import os
import random
import math

def vecCheck(tVec):
	if type(tVec) in (sf.Vector2, tuple, list):
		return True
	else:
		return False

def createCorners(center,height,width):
	tL=[center[0]-height/2,center[1]-width/2]
	bR=[center[0]+height/2,center[1]+width/2]
	return [tL,bR]

def inVPlane(xCoord,tL,bR): # tL and bR should be the top left and bottom right 
							# coordinates of the object
	if (xCoord>=tL[0] and xCoord<=bR[0]):
		return True
	else:
		return False

def inHPlane(yCoord,tL,bR): # tL and bR should be the top left and bottom right 
							# coordinates of the object
	if (yCoord>=tL[1] and yCoord<=bR[1]):
		return True
	else:
		return False

def pointIn(pVec,tL,bR): # tL and bR should be the top left and bottom right 
						 # coordinates of the object
	if inVPlane(pVec[0],tL,bR) and inHPlane(pVec[1],tL,bR):
		return True
	else:
		return False

def main():
	box=[]
	boxAttr=[] # contains arrays->[topLeft,bottomRight]
	for i in range(2):
		box.append(sf.RectangleShape())
		box[i].size=(96,96)
		box[i].origin=(48,48)
		box[i].outline_color=sf.Color.BLACK
		box[i].outline_thickness=1

	box[0].fill_color=sf.Color.RED
	box[1].fill_color=sf.Color.YELLOW

	box[0].position=(96,96)
	box[1].position=(288,96)

	for i in range(len(box)):
		boxAttr.append([])
		tL=[box[i].position.x-box[i].size.x/2,box[i].position.y-box[i].size.y/2]
		bR=[box[i].position.x+box[i].size.x/2,box[i].position.y+box[i].size.y/2]
		boxAttr[i].append(tL)
		boxAttr[i].append(bR)

	window=sf.RenderWindow(sf.VideoMode(1000,600),"Test")
	window.framerate_limit=60

	while window.is_open:
		window.clear(sf.Color(50,100,150,255))
		
		for event in window.events:

			if type(event)==sf.CloseEvent:
				window.close()
			if type(event) == sf.KeyEvent: # Pressed Key
				if event.code is sf.Keyboard.SPACE:
					for i in range(len(box)):
						if pointIn(sf.Mouse.get_position(window),boxAttr[i][0],boxAttr[i][1]):
							box[i].position=sf.Mouse.get_position(window)	
							boxAttr[i]=createCorners(box[i].position,box[i].size.x,box[i].size.y)

			if type(event) == sf.KeyEvent and event.released: # Released Key
				if event.code is sf.Keyboard.SPACE:
					print("Box Released")

			

		#print(sf.Mouse.get_position(window))
		#cPos=sf.Mouse.get_position(window)
		#print(pointIn(cPos,boxAttr[0][0],boxAttr[0][1]))

		for i in range(2):
			window.draw(box[i])

		window.display()

if __name__=='__main__':
	main()
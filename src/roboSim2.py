import sfml
import os
import sys
import random
import math

from utilFunctions import *

import gRobot
import sensors
import motors
import servos

import interface

#--------------------TODO--------------------#
#
#
#
# 1. Write todo
#	a. These aren't really in an order
# 2. Come up with inteface
# 	a. probably something like the link interface
# 3. write inteface code
# 4. write motor/servo code
# 	a. 
# 5. write sensor code
#	a. characterize the analog sensors
#	b. find a way to make the sensors have a type
#		i. subclasses for each sensor?
# 6. brainstorm how to draw the bot
#	a. have position as part of the members
#	b. make sprites for each component?
# 7. write docs
#	a. get better at LaTeX
# 8. Make sure to commit
#	a. at least make an effort at good commit messages
# 9. write code to make courses/fields
#	a. write how the bot will interact with these
#		i. pass in a 'context' (the window/scene) that updates
#	b. have a config file that defines the scene
# 10. make sprites
#	a. button sprites
# 
#
#
#--------------------TODO--------------------#

def main():
	print("Robo Sim v2 \n")

	lSprite=sprite('../sprites/leverSprite.cfg')
	gSprite=sprite('../sprites/genericSprite.cfg')
	mSprite=sprite('../sprites/motorSprite.cfg')

	config=(4,4,6,6)
	link=gRobot.robot(config)

	servo0=servos.servo(0)
	servo1=servos.servo(1)
	servo2=servos.servo(2)
	servo3=servos.servo(3)

	motor0=motors.motor(0,0,1000,0,mSprite)
	motor1=motors.motor(1,0,1000,0,mSprite)

	lMot=motors.motor(2,50,1000,0,mSprite)
	rMot=motors.motor(3,50,1000,0,mSprite)

	link.addMotors(motor0,motor1)
	link.addServos(servo0,servo1,servo2,servo3)

	link.addDriveMotors(lMot,rMot,10)

	rScreen=interface.robotScreen()

	print('')

	try: 
		robot.draw()
	except NameError:
		print("Not a valid bot")

	try:
		link.enableServos()
	except NameError:
		print("Not a valid bot")

	window=interface.simScreen(1600,900)
#
#	while window.is_open:
#		window.clear(window.color)
#
#		for event in window.events:
#			if type(event)==sfml.CloseEvent:
#				window.close()
#
#		window.draw(lSprite)
#
#		window.display()

	link.defineContext(window)

	link.update()

	print('')

if __name__=='__main__':
	main()
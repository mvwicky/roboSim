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
#		i. make  sprites
# 7. write docs
#	a. get better at LaTeX
# 8. Make sure to commit
#	a. at least make an effort at good commit messages
# 9. write code to make courses/fields
#	a. write how the bot will interact with these
#
# 
#
#
#--------------------TODO--------------------#

def main():
	print("Robo Sim v2")
	
	config=(4,4,6,6)

	link=gRobot.robot(config)

	tSprite=sprite('../sprites/leverSprite.cfg')
	gSprite=sprite('../sprites/genericSprite.cfg')
	mSprite=sprite('../sprites/motorSprite.cfg')

	servo0=servos.servo(0)
	servo1=servos.servo(1)
	servo2=servos.servo(2)
	servo3=servos.servo(3)

	motor0=motors.motor(0,0,1000,0,mSprite)
	motor1=motors.motor(1,0,1000,0,mSprite)
	motor2=motors.motor(2,0,1000,0,mSprite)
	motor3=motors.motor(3,0,1000,0,mSprite)

	link.addServo(servo3)
	link.addServo(servo2)
	link.addServo(servo0)
	link.addServo(servo1)

	link.addMotor(motor0)
	link.addMotor(motor1)
	link.addMotor(motor2)
	link.addMotor(motor3)

	print('\n')

	try: 
		robot.draw()
	except NameError:
		print("Not a valid bot")

	try:
		link.enableServos()
	except NameError:
		print("Not a valid bot")

#	window=interface.simScreen(1600,900)
#
#	while window.is_open:
#		window.clear(window.color)
#
#		for event in window.events:
#			if type(event)==sfml.CloseEvent:
#				window.close()
#
#		window.display()

	print("")
if __name__=='__main__':
	main()
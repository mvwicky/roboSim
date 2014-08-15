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
	print("")

	window=interface.simScreen(1600,900)

	config=(4,4,6,6)

	link=gRobot.robot(config)

	print link.config

	servo0=servos.servo(0)
	servo1=servos.servo(1)
	servo2=servos.servo(2)
	servo3=servos.servo(3)

	link.addServo(servo3)
	link.addServo(servo2)
	link.addServo(servo0)
	link.addServo(servo1)

	for i in link.servos:
		print i.port
	
	print '\n' ,  "Num Servos:" , len(link.servos)

	print("")

	try: 
		robot.draw()
	except NameError:
		print("Not a valid bot")

	while window.is_open:
		window.clear(window.color)

		for event in window.events:
			if type(event)==sfml.CloseEvent:
				window.close()

		window.display()

	print("")
if __name__=='__main__':
	main()
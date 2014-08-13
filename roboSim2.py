import sfml
import os
import sys
import random
import math

from utilFunctions import *
import gRobot

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
#		i. make sprites
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
	try: 
		robot.sample()
	except NameError:
		print("Not a valid bot")

if __name__=='__main__':
	main()
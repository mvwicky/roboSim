class analogSensor(object):
	"""Generic Analog Sensor Class
	   Goes from a value of 0-1024"""
	def __init__(self,port):
		self.port=port
		self.value=
	
	def sample(self):
	"""Get a single value from the sensor"""
		pass
	
	def avgSample(self,numSamples):
	"""Gets a number of samples and averages them"""
		pass

class digitalSensor(object):
	"""Generic Digital Sensor Class
	   Is either off(0) or on(1)"""
	def __init__(self,port):
		self.port=port
		self.value=0

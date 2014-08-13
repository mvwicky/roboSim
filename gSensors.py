class analogSensor(object):
	"""Generic Analog Sensor Class
	   Goes from a value of 0-1024"""
	def __init__(self,port):
		self.port=port
		self.value=sample()
	
	def sample(self):
		"""Returns the current value of the sensor """
		pass
	
	def avgSample(self,numSamples):
		"""Returns the average of a number of samples """
		ret=0
		for i in range(numSamples):
			ret+=sample()
		return (ret/numSamples)

class digitalSensor(object):
	"""Generic Digital Sensor Class
	   Is either off(0) or on(1)"""
	def __init__(self,port):
		self.port=port
		self.value=0

	def sample(self):
		pass


class rangeFinder(analogSensor):
	def __init__(self,port):
		super(rangeFinder,self).__init__(port)
	def sample(self):
	# some math function will define the value returned	
		pass
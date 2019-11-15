import pyglet
import random
class Brain():
	step=0
	directions=[]
	def __init__(self,size):
		self.directions=[]
		self.randomize(size)

	def randomize(self,size):
		for i in range(size):
			self.directions.append(random.randrange(4))
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

	def clone(self):
		clone = Brain(len(self.directions))
		clone.directions = []
		for i in range(len(self.directions)):
			clone.directions.append(self.directions[i])
		return clone

	def mutate(self):
		mutationrate = 0.01
		for i in range(len(self.directions)):
			rand = random.random()
			if rand < mutationrate:
				self.directions[i] = random.randrange(4)
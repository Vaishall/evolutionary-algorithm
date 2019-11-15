import pyglet
import mice
import random
class Population:
	mice_list=[]
	generation = 1
	fitnessTotal = 0
	best_mouse = 0
	minstep = 50

#------------------------------------------------------------------------

	def __init__(self,size):
		for i in range(size):
			new_mouse = mice.mice()
			self.mice_list.append(new_mouse)
		self.fitnessTotal = 0.0

	def show(self):
		for i in range(1,len(self.mice_list)):
			self.mice_list[i].show()
		self.mice_list[0].show()

	def update(self):
		for mouse in self.mice_list:
			if mouse.brain.step > self.minstep:
				mouse.dead = True
			else:
				mouse.update()

#--------------------------------------------------------------------------

	def calculateFitness(self):
		for mouse in self.mice_list:
			mouse.calculateFitness()

	def allmicedead(self):
		for mouse in self.mice_list:
			if not(mouse.dead):
				return False
		return True

	def fitnessSum(self):
		self.fitnessTotal = 0
		for mouse in self.mice_list:
			self.fitnessTotal += mouse.fitness

#--------------------------------------------------------------------------

	def naturalSelection(self):
		new_mice = []
		self.findbestmouse()
		self.fitnessSum()

		new_mice.append(self.mice_list[self.best_mouse].getBaby())
		new_mice[0].mouse = pyglet.sprite.Sprite(pyglet.image.load('best.png'), x=0, y=500-50)
		for i in range(len(self.mice_list)-1):
			parent = self.selectParents()
			baby=parent.getBaby()
			new_mice.append(baby)

		self.mice_list = new_mice
		self.generation += 1


	def selectParents(self):
		rand = random.uniform(0,self.fitnessTotal)
		runningSum = 0
		for mouse in self.mice_list:
			runningSum += mouse.fitness
			if runningSum > rand:
				return mouse

	def mutateBabies(self):
		for i in range(1,len(self.mice_list)):
			self.mice_list[i].brain.mutate()

#--------------------------------------------------------------------------

	def findbestmouse(self):
		max_fitness = 0
		best_index = 0
		for i in range(len(self.mice_list)):
			if self.mice_list[i].fitness > max_fitness:
				max_fitness = self.mice_list[i].fitness
				best_index = i
		self.best_mouse = best_index
		self.mice_list[self.best_mouse].isBest = True
		if self.mice_list[self.best_mouse].win == True:
			self.minstep = self.mice_list[self.best_mouse].brain.step
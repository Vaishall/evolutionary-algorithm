import pyglet
import Brain
class mice():
	mouse_img = pyglet.image.load('mouse.png')
	best_img = pyglet.image.load('best.png')
	isBest = False

#--------------------------------------------------------------------------------------------------------

	def __init__(self):
		self.brain = Brain.Brain(40)
		self.mouse = pyglet.sprite.Sprite(img=self.mouse_img, x=0, y=500-50)
		self.dead = False
		self.win = False
		self.cat = False
		self.fitness = 0.0

	def show(self):
		self.mouse.draw()
	def move(self):
		if len(self.brain.directions) > self.brain.step:
			option = self.brain.directions[self.brain.step]
			self.brain.step += 1
			if option == 0:
				if self.mouse.x > 0:
					self.mouse.x -= 50
			elif option == 1:
				if self.mouse.x < 450:
					self.mouse.x += 50
			elif option == 2:
				if self.mouse.y < 450:
					self.mouse.y +=50
			elif option == 3:
				if self.mouse.y > 0:
					self.mouse.y -= 50
		else:
			self.dead = True

	def update(self):
		if (not(self.dead) and not(self.win)):
			self.move()
			self.show()
			cat_positions = [(4,1),(4,2),(7,2),(8,2),(7,3),(8,3),(1,4),(2,4),(5,4),(6,4),(7,4),
							(8,4),(9,4),(10,4),(9,5),(5,7),(1,8),(2,8),(9,8),(3,9),(9,10)]
			if (1+self.mouse.x/50,10-self.mouse.y/50) in cat_positions:
				self.dead = True
				self.cat = True
			if (self.mouse.x, self.mouse.y) == (450,0):
				print('win')
				self.win = True
				self.dead = True

#--------------------------------------------------------------------------------------------------------

	def calculateFitness(self):
		if self.win == True:
			self.fitness = 1.0 + 10000.0/(self.brain.step*self.brain.step)
		elif self.cat == True:
			distsq = (((self.mouse.x-450)*(self.mouse.x-450))+(self.mouse.y*self.mouse.y))/2500
			self.fitness = 1.0/(distsq*10000*10000)
		else:
			distsq = (((self.mouse.x-450)*(self.mouse.x-450))+(self.mouse.y*self.mouse.y))/2500
			self.fitness = 1.0/(distsq)

	def getBaby(self):
		baby = mice()
		#if self.isBest == True:
		#	baby.mouse = pyglet.sprite.Sprite(img=self.best_img, x=0, y=500-50)
		baby.brain = self.brain.clone()
		return baby
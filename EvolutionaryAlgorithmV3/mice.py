import pyglet
import Brain
class mice():
	mouse_img = pyglet.image.load('mouse.png')
	#mouse = pyglet.sprite.Sprite(img=mouse_img, x=0, y=500-50)
	dead = False
	def __init__(self):

		self.brain = Brain.Brain(30)
		#mouse_img = pyglet.image.load('mouse.png')
		self.mouse = pyglet.sprite.Sprite(img=self.mouse_img, x=0, y=500-50)
		#position = (1,1)
		#poschange = [0,0]

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
			print('dead')

	def update(self):
		if not(self.dead):
			self.move()
			self.show()
			cat_positions = [(4,1),(4,2),(7,2),(8,2),(7,3),(8,3),(1,4),(2,4),(3,4),(5,4),(6,4),(7,4),
							(8,4),(9,4),(10,4),(9,5),(5,7),(1,8),(2,8),(9,8),(3,9),(9,9),(9,10)]
			if (1+self.mouse.x/50,10-self.mouse.y/50) in cat_positions:
				print('meow')
				self.dead=True
			#if (player.x, player.y) == (450,0):
			#	print('win')
			#	win=True
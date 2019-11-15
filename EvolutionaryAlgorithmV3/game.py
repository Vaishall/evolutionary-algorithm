import pyglet
from pyglet.window import key
import Brain

board = pyglet.image.load('board.png')
black_cat = pyglet.image.load('cat_black.png')
white_cat = pyglet.image.load('cat_white.png')
cheese_pic = pyglet.image.load('cheese.png')
window = pyglet.window.Window(board.width, board.height)
catbatch = pyglet.graphics.Batch()
playerbatch = pyglet.graphics.Batch()




#------------------------------------------------------------------------------------------------------------


class Population:
	mice_list=[]
	def __init__(self,size):
		for i in range(size):
			new_mouse = mice()
			self.mice_list.append(new_mouse)

	def show(self):
		for mouse in self.mice_list:
			mouse.show()

	def update(self):
		for mouse in self.mice_list:
			mouse.update()
		print('done')


#----------------------------------------------------------------------------------------------------------


class mice():
	mouse_img = pyglet.image.load('mouse.png')
	#mouse = pyglet.sprite.Sprite(img=mouse_img, x=0, y=500-50, batch=playerbatch)
	dead = False
	def __init__(self):

		self.brain = Brain.Brain(30)
		#mouse_img = pyglet.image.load('mouse.png')
		self.mouse = pyglet.sprite.Sprite(img=self.mouse_img, x=0, y=500-50, batch=playerbatch)

	@window.event
	def show(self):
		self.mouse.draw()
		#print("hi")

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
		print(f"{self.mouse.x},{self.mouse.y}")

	def update(self):
		if not(self.dead):
			self.move()
			#self.show()
			cat_positions = [(4,1),(4,2),(7,2),(8,2),(7,3),(8,3),(1,4),(2,4),(3,4),(5,4),(6,4),(7,4),
							(8,4),(9,4),(10,4),(9,5),(5,7),(1,8),(2,8),(9,8),(3,9),(9,9),(9,10)]
			if (1+self.mouse.x/50,10-self.mouse.y/50) in cat_positions:
				print('meow')
				self.dead=True
			#if (player.x, player.y) == (450,0):
			#	print('win')
			#	win=True






#-------------------------------------------------------------------------------------------------------------------------





generation_count=0
generation_label = pyglet.text.Label(text="Gen:"+str(generation_count), x=0, y=2,
									color=(0,0,0,255))

cat_positions = [(4,1),(4,2),(7,2),(8,2),(7,3),(8,3),(1,4),(2,4),(3,4),(5,4),(6,4),(7,4),
				(8,4),(9,4),(10,4),(9,5),(5,7),(1,8),(2,8),(9,8),(3,9),(9,9),(9,10)]

cats = []
for (x,y) in cat_positions:
	if (x+y)%2 == 0:
		new_cat = pyglet.sprite.Sprite(img=white_cat, x=(x-1)*50, y=500-y*50, batch=catbatch)
		cats.append(new_cat)
	elif (x+y)%2 == 1:
		new_cat = pyglet.sprite.Sprite(img=black_cat, x=(x-1)*50, y=500-y*50, batch=catbatch)
		cats.append(new_cat)

cheese = pyglet.sprite.Sprite(img=cheese_pic, x=9*50, y=0)
players = Population(10)

@window.event
def on_draw():
	window.clear()
	board.blit(0,0)
	generation_label.draw()
	catbatch.draw()
	playerbatch.draw()
	cheese.draw()
	#players.show()


game_objects=[players]

@window.event
def update(dt):
	for obj in game_objects:
		obj.update()
		obj.show()
		playerbatch.draw()

#handler = mice()
#window.push_handlers(handler)




if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1)
	pyglet.app.run()
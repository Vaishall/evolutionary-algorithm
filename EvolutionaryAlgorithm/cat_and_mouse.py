import pyglet
import Population


board = pyglet.image.load('board.png')
cat = pyglet.image.load('cat.png')
cheese_pic = pyglet.image.load('cheese.png')
window = pyglet.window.Window(board.width, board.height)
catbatch = pyglet.graphics.Batch()

cat_positions = [(4,1),(4,2),(7,2),(8,2),(7,3),(8,3),(1,4),(2,4),(5,4),(6,4),(7,4),
				(8,4),(9,4),(10,4),(9,5),(5,7),(1,8),(2,8),(9,8),(3,9),(9,10)]

cats = []
for (x,y) in cat_positions:
	new_cat = pyglet.sprite.Sprite(img=cat, x=(x-1)*50, y=500-y*50, batch=catbatch)
	cats.append(new_cat)

cheese = pyglet.sprite.Sprite(img=cheese_pic, x=9*50, y=0)
players = Population.Population(50)

generation_label = pyglet.text.Label(text="Gen:  "+str(players.generation), x=0, y=2,
									color=(0,255,0,255))


game_objects=[players]
@window.event
def update(dt):
	for obj in game_objects:
		obj.update()
	if players.allmicedead() == True:
		#genetic algorithm
		players.calculateFitness()
		players.naturalSelection()
		players.mutateBabies()
		generation_label.text = "Gen:   " + str(players.generation)
		generation_label.draw()


@window.event
def on_draw():
	window.clear()
	board.blit(0,0)
	generation_label.draw()
	catbatch.draw()
	cheese.draw()
	players.show()

pyglet.clock.schedule_interval(update, 1/30.0)


pyglet.app.run()
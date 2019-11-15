import pyglet
import Player
import physicalobject
from pyglet.window import key

board = pyglet.image.load('board.png')
black_cat = pyglet.image.load('cat_black.png')
white_cat = pyglet.image.load('cat_white.png')
cheese_pic = pyglet.image.load('cheese.png')
mouse = pyglet.image.load('mouse.png')
window = pyglet.window.Window(board.width, board.height)
catbatch = pyglet.graphics.Batch()

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
player = pyglet.sprite.Sprite(img=mouse, x=0, y=500-50)
player_ship=Player.Player(x=0, y=500-50)
window.push_handlers(player_ship.key_handler)

game_objects = [player_ship]

@window.event
def update(dt):
	for obj in game_objects:
		obj.update(dt)

@window.event
def on_draw():
	window.clear()
	board.blit(0,0)
	generation_label.draw()
	catbatch.draw()
	cheese.draw()
	player_ship.draw()
	#player.draw()




pyglet.clock.schedule_interval(update, 1/120.0)



pyglet.app.run()
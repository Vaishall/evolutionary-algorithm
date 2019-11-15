import pyglet
from pyglet.window import key
import physicalobject
class Player(physicalobject.PhysicalObject):
	def __init__(self, *args, **kwargs):
		mouse = pyglet.image.load('mouse.png')
		super().__init__(img=mouse, *args, **kwargs)
		self.speed=50.0
		self.key_handler = key.KeyStateHandler()

	def update(self,dt):
		super(Player, self).update(dt)
		if self.key_handler[key.LEFT]:
			self.x_change -= self.speed * dt
		if self.key_handler[key.RIGHT]:
			self.x_change += self.speed * dt
		if self.key_handler[key.UP]:
			self.y_change += self.speed * dt
		if self.key_handler[key.DOWN]:
			self.y_change -= self.speed * dt


import pyglet
class PhysicalObject(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.x_change, self.y_change = 0.0, 0.0
	def update(self,dt):
		self.x += self.x_change * dt
		self.y += self.y_change * dt
		self.check_bounds()
	def check_bounds(self):
		min_x = 0
		min_y = 0
		max_x = 450
		max_y = 450
		if self.x < min_x:
			self.x = min_x
		elif self.x > max_x:
			self.x = max_x
		if self.y < min_y:
			self.y = min_y
		elif self.y > max_y:
			self.y = max_y
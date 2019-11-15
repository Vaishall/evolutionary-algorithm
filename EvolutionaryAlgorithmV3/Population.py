import pyglet
import mice
class Population:
	mice_list=[]
	def __init__(self,size):
		for i in range(size):
			new_mouse = mice.mice()
			self.mice_list.append(new_mouse)

	def show(self):
		for mouse in self.mice_list:
			mouse.show()

	def update(self):
		for mouse in self.mice_list:
			mouse.update()
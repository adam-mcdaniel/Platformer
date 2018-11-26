from random import randint
from easy_mobile.setup import *

screen = setup(
		level_width=2000,
		level_height=2000,
		title='Hello World!'
		)

class SquirmyBlock(Sprite):
	def __init__(self, x, y):
		super().__init__(x, y, "block.png")

	def update(self, screen):
		self.move(
                	randint(-9, 10),
                	randint(-9, 10)
                	)



block = SquirmyBlock(500, 500)
screen.append(block)

for _ in range(5):
	screen.append(SquirmyBlock(randint(250, 750), randint(250, 750)))


def event_loop():
	# focus camera on block
	screen.focus(block)

screen.run(event_loop)


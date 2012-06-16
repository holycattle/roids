import pyglet
import util

class PhysicalObject(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(PhysicalObject, self).__init__(*args, **kwargs)
		self.velocity_x, self.velocity_y = 0.0, 0.0
		self.dead = False

	def update(self, dt):
		self.x += self.velocity_x * dt
		self.y += self.velocity_y * dt
		self.check_bounds()

	def check_bounds(self):
		min_x = -self.image.width/2
		min_y = -self.image.height/2
		max_x = 800 + self.image.width/2
		max_y = 600 + self.image.height/2

		if self.x < min_x:
			self.x = max_x
		elif self.x > max_x:
			self.x = min_x
		if self.y < min_y:
			self.y = max_y
		if self.y > max_y:
			self.y = min_y

	def collides(self, other_object):
		collision_dist = self.image.width/2 + other_object.image.width/2
		actual_dist = util.distance(self.position, other_object.position)
	
		return (actual_dist <= collision_dist)

	def handle_collision(self, other_object):
		self.dead = True
		other_object.dead = True
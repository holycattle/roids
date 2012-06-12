import physicalobject, resources
from pyglet.window import key
import pyglet
import math

class Player(physicalobject.PhysicalObject):

	def __init__(self, *args, **kwargs):
		super(Player, self).__init__(img=resources.player_image, *args, **kwargs)
		self.thruster_sprite = pyglet.sprite.Sprite(img=resources.thruster_image, *args, **kwargs)
		self.thruster_sprite.visible = False
		self.thrust = 300.0
		self.rotate_speed = 200.0
		self.key_handler = key.KeyStateHandler()

	def update(self, dt):
		super(Player, self).update(dt)

		if self.key_handler[key.LEFT]:
			self.rotation -= self.rotate_speed * dt
		if self.key_handler[key.RIGHT]:
			self.rotation += self.rotate_speed * dt
		#brilliant code right here:
		if self.key_handler[key.UP]:
			angle_radians = -math.radians(self.rotation)
			force_x = math.cos(angle_radians) * self.thrust * dt
			force_y = math.sin(angle_radians) * self.thrust * dt
			self.thruster_sprite.visible = True
			self.thruster_sprite.rotation = self.rotation
			self.thruster_sprite.x = self.x
			self.thruster_sprite.y = self.y
			self.velocity_x += force_x
			self.velocity_y += force_y
		else:
			self.thruster_sprite.visible = False

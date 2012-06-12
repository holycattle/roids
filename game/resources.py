#should be inside the game/ folder
import pyglet

pyglet.resource.path = ['resources']
pyglet.resource.reindex()

player_image = pyglet.resource.image("player.png")
bullet_image = pyglet.resource.image("bullet.png")
asteroid_image = pyglet.resource.image("asteroid.png")
thruster_image = pyglet.resource.image("engine_flame.png")

thruster_image.anchor_x = thruster_image.width * 1.5
thruster_image.anchor_y = thruster_image.height / 2

def center_image(image):
	image.anchor_x = image.width/2
	image.anchor_y = image.height/2

center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)
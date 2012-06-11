import pyglet, random, math
import resources

def asteroids(num_asteroids, player_position, batch=None):
	asteroids = []
	for i in range(num_asteroids):
		asteroid_x, asteroid_y = player_position
		while get_distance((asteroid_x, asteroid_y), player_position) < 100:
			asteroid_x = random.randint(0, 800)
			asteroid_y = random.randint(0, 600)
		new_asteroid = pyglet.sprite.Sprite(img=resources.asteroid_image, x=asteroid_x, y=asteroid_y, batch=batch)
		new_asteroid.rotation = random.randint(0, 360)
		asteroids.append(new_asteroid)
	return asteroids

def player_lives(num_icons, batch=None):
	player_lives = []
	for i in range(num_icons):
		new_sprite = pyglet.sprite.Sprite(img=resources.player_image, x=785-i*30, y=585, batch=batch)
		new_sprite.scale = 0.5
		player_lives.append(new_sprite)
	return player_lives

def get_distance(p1=(0, 0), p2=(0,0)):
	return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
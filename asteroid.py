import pyglet,  random
from game import resources, load

game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Game 1", x=400, y=575, anchor_x='center', batch=main_batch)

player_ship = pyglet.sprite.Sprite(img = resources.player_image, x=400, y=300, batch=main_batch)
asteroids = load.asteroids(3, player_ship.position, main_batch)
lives = load.player_lives(2, main_batch)

@game_window.event
def on_draw():
	game_window.clear()
	main_batch.draw()

if __name__ == '__main__':
	pyglet.app.run()

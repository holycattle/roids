import pyglet,  random
from game import resources, load, physicalobject, player

game_window = pyglet.window.Window(800, 600)

main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="Game 1", x=400, y=575, anchor_x='center', batch=main_batch)

player_ship = player.Player(x=400, y=300, batch=main_batch)
asteroids = load.asteroids(3, player_ship.position, main_batch)
lives = load.player_lives(2, main_batch)

#add player_ship into the Event Queue
game_window.push_handlers(player_ship)

game_objects = [player_ship] + asteroids

#re-draws the objects every time the screen refreshes
@game_window.event
def on_draw():
	game_window.clear()
	main_batch.draw()

def update(dt):
	for obj in game_objects:
		obj.update(dt)

if __name__ == '__main__':
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()

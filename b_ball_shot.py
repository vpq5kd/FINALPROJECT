# This is an early working example
# For the image boxes, substitute in images of your own,
# or convert them to from_color
#
import uvage

camera = uvage.Camera(800, 600)

# scenery
background = uvage.from_image(400, 300, 'uva_court.jpg')
background.scale_by(2.2)
court = uvage.from_color(400, 500, 'blue', 400, 50)
backboard = uvage.from_color(475, 400, 'white', 30, 200)
hoop = uvage.from_image(445, 350, 'hoop.png')
hoop.scale_by(0.3)
scenery = [background, court, backboard, hoop]  # Things that are stationary
obstacles = [court, backboard]  # things that are "solid"

# interactive
ball = uvage.from_circle(300, 465, 'orangered', 10)

# stats
score = 0
lives = 3

# physics
gravity = 0.75
jump_speed = 20

# other
scored_since_landed = False


def draw_scenery():
	"""Draw all the stationary items"""
	for item in scenery:
		camera.draw(item)


def draw_stats():
	"""draws the gameplay information (lives, score)"""
	scorebox = uvage.from_text(75, 25, "score: " + str(score), 36, 'red')
	camera.draw(scorebox)
	for i in range(lives):
		heart = uvage.from_image(775, 25, 'heart2.png')
		heart.scale_by(0.5)
		heart.x -= 50 * i
		heart.scale_by(0.5)
		camera.draw(heart)


def move_ball():
	"""Determines where the ball should be by checking for user input and obstacles"""
	global scored_since_landed
	if uvage.is_pressing('right arrow'):
		ball.speedx += 1
	if uvage.is_pressing('left arrow'):
		ball.speedx -= 1
	for obstacle in obstacles:
		if ball.bottom_touches(obstacle):
			scored_since_landed = False
			if uvage.is_pressing('up arrow'):
				ball.speedy = -jump_speed
	ball.speedy += gravity
	ball.move_speed()
	for obstacle in obstacles:
		ball.move_to_stop_overlapping(obstacle)


def points_scored():
	"""Checks if the user scored a basket this tick"""
	global scored_since_landed
	if ball.touches(hoop) and not scored_since_landed and ball.speedy > 0:
		scored_since_landed = True
		return 2
	return 0


def out_of_bounds():
	"""checks if the ball is out of bounds"""
	return ball.y > 600 or (ball.touches(hoop) and ball.speedy < 0)


def reset_ball():
	"""replace the ball when it's out of bounds"""
	ball.x = 400
	ball.y = 300
	ball.speedx = 0
	ball.speedy = 0


def game_over():
	"""checks if there is a game over, draws things based on that"""
	if lives == 0:
		camera.draw(uvage.from_text(400, 300, 'You Lose', 42, 'white', True))
		camera.display()
		return True
	return False


def tick():
	global score, lives
	camera.clear('black')
	if game_over():
		return
	draw_scenery()
	draw_stats()
	move_ball()
	score += points_scored()
	if out_of_bounds():
		lives -= 1
		reset_ball()
	camera.draw(ball)
	camera.display()


uvage.timer_loop(30, tick)

import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

def main():
	# Initializes pygame
	pygame.init()
	
	#Screen setup
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	screen_color = (0, 0, 0)

	#Clock setup
	clock = pygame.time.Clock()
	dt = 0

	score = 0

	#Player setup
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	player = Player(x, y, PLAYER_RADIUS)

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()

	Shot.containers = (shots, updatable, drawable)

	#Game loop
	while True:
		for event in pygame.event.get():
			#X button works on window
			if event.type == pygame.QUIT:
				return
		
		updatable.update(dt)

		for obj in asteroids:
			if obj.collide(player) == True:
				print(f"Game Over! Your score was {score}")
				quit()
			else:
				pass

			for shot in shots:
				if obj.collide(shot) == True:
					shot.kill()
					obj.split()
					score += 1

		#Makes screen black
		screen.fill(screen_color)
		
		#Update player
		for draw in drawable:
			draw.draw(screen)
		

		#Render game
		pygame.display.flip()
		# Sets clock
		dt = clock.tick(60) / 1000
	

	print("Starting Asteroids!")
	print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')

if __name__ == '__main__':
	main()

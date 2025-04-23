import pygame
from constants import *
from player import *


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

	#Player setup
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

	Player.containers = (updatable, drawable)
	player = Player(x, y, PLAYER_RADIUS)
	

	#Game loop
	while True:
		for event in pygame.event.get():
			#X button works on window
			if event.type == pygame.QUIT:
				return
		
		updatable.update(dt)

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

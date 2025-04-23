import pygame
from constants import *





def main():
	# Initializes pygame
	pygame.init()
	
	#Screen setup
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	screen_color = (0, 0, 0)

	#Clock setup
	clock = pygame.time.Clock()
	dt = 0

	#Game loop
	while True:
		for event in pygame.event.get():
			#X button works on window
			if event.type == pygame.QUIT:
				return

		#Makes screen black
		screen.fill(screen_color)
		pygame.display.flip()
		# Sets clock
		dt = clock.tick(60) / 1000
	

	print("Starting Asteroids!")
	print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')

if __name__ == '__main__':
	main()

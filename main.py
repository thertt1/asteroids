import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_color = (0, 0, 0)

while True:
	for event in pygame.event.get():
    	if event.type == pygame.QUIT:
        	return
	screen.fill(screen_color)
	pygame.display.flip()

def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')

if __name__ == '__main__':
	main()

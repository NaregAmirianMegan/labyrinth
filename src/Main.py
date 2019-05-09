import pygame, os
from pygame.locals import *

from Game import Game

print("Game loading...")

#set window position
x = 500
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#setup pygame
pygame.init()
#setup text font
pygame.font.init()

#set game constants
#set window size
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

#create pygame display and frame clock
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Labyrinth')

game_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
			[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
			[0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
			[0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
			[0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
			[0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
			]

game = Game(screen, WINDOW_WIDTH, WINDOW_HEIGHT, game_map)
game.run()
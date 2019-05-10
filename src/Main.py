import pygame, os
from pygame.locals import *

from Game import Game
from InstructionScreen import InstructionScreen

print("Game loading...")

#set window position
x = 500
y = 100
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#setup pygame
pygame.init()
#setup text font
pygame.font.init()
myFont = pygame.font.SysFont('Comic Sans MS', 29)

#set game constants
#set window size
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

#create pygame display and frame clock
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Labyrinth')

game_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
			[0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
			[0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
			[0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
			[0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
			[0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
			[0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
			]

instructions = "Theseus. Your goal is to make it through the Labyrinth! watch out for the red dots flying over the Labyrinth. They will fly down and ask you to make a choice. Choose wrong and you will not survive. Use the arrow keys to move and beware of gravity pulling you down. DON'T touch the edge of the maze, that is also fatal. Good Luck Theseus! Aegeus awaits!"

game = Game(screen, WINDOW_WIDTH, WINDOW_HEIGHT, game_map, myFont)
InstructionScreen(game, instructions).run()
#External Imports
import pygame, os, time, random
from pygame.locals import *

class WinScreen:
	def __init__(self, game, elapsed):
		self.game = game
		self.quit = False
		self.elapsed = elapsed

	def run(self):

		clock = pygame.time.Clock()

		mouse_in_box1 = False
		mouse_in_box2 = False

		width = 100
		height = 50
		xPos = self.game.width/2 - width/2
		yPos1 = self.game.height/2 - height/2 - 3
		yPos2 = self.game.height/2 + height/2 + 3

		content = self.game.font.render("Congrats you made it! It took you " + str(self.elapsed) + " second(s)!", False, (255, 255, 255))
		label1 = self.game.font.render("QUIT", False, (255, 255, 255))
		label2 = self.game.font.render("PLAY", False, (255, 255, 255))

		while not self.quit:

			clock.tick(30)

			self.game.screen.fill((0, 0, 0))

			#display text and answer buttons
			if mouse_in_box1:
				pygame.draw.rect(self.game.screen, (255, 0, 0), (xPos, yPos1, width, height), 0)
				self.game.screen.blit(label1, (xPos+width/2-25, yPos1+height/2-10))
			else:
				pygame.draw.rect(self.game.screen, (100, 100, 100), (xPos, yPos1, width, height), 0)
				self.game.screen.blit(label1, (xPos+width/2-25, yPos1+height/2-10))

			if mouse_in_box2:
				pygame.draw.rect(self.game.screen, (0, 255, 0), (xPos, yPos2, width, height), 0)
				self.game.screen.blit(label2, (xPos+width/2-25, yPos2+height/2-10))
			else:
				pygame.draw.rect(self.game.screen, (100, 100, 100), (xPos, yPos2, width, height), 0)
				self.game.screen.blit(label2, (xPos+width/2-25, yPos2+height/2-10))

			self.game.screen.blit(content, (10, 10))

			#check for mouse over and button click
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
				    pygame.quit()
				    quit()

				if self.mouse_over_box(pygame.mouse.get_pos(), xPos, yPos1, width, height):
					mouse_in_box1 = True
				else:
					mouse_in_box1 = False
					
				if self.mouse_over_box(pygame.mouse.get_pos(), xPos, yPos2, width, height):
					mouse_in_box2 = True
				else:
					mouse_in_box2 = False

				if pygame.mouse.get_pressed()[0]:
					if mouse_in_box1:
						self.answered = True
						print("quit")
						pygame.quit()
						quit()
					elif mouse_in_box2:
						self.answered = True
						print("play again")
						self.game.run()

			pygame.display.update()


	def mouse_over_box(self, mouse_pos, xPos, yPos, width, height):
		return mouse_pos[0] > xPos and mouse_pos[0] < xPos+width and mouse_pos[1] > yPos and mouse_pos[1] < yPos+height

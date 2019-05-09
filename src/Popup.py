#External Imports
import pygame, os, time, random
from pygame.locals import *

class Popup:
	def __init__(self, game, content):
		self.answered = False
		self.game = game
		self.content = content

	def run(self):

		clock = pygame.time.Clock()

		width = 100
		height = 50
		xPos = self.game.width/2 - width/2
		yPos1 = self.game.height/2 - height
		yPos2 = self.game.height/2 + height

		label1 = self.game.font.render("NO", False, (255, 255, 255))
		label2 = self.game.font.render("YES", False, (255, 255, 255))

		while not self.answered:

			clock.tick(30)

			mouse_in_box1 = False
			mouse_in_box2 = False

			self.game.screen.fill((0, 0, 0))
			#display text and answer buttons
			pygame.draw.rect(self.game.screen, (100, 100, 100), (xPos, yPos1, width, height), 0)
			pygame.draw.rect(self.game.screen, (100, 100, 100), (xPos, yPos2, width, height), 0)
			self.game.screen.blit(label1, (xPos+width/2-10, yPos1+height/2-10))
			self.game.screen.blit(label2, (xPos+width/2-1, yPos2+height/2-10))

			#check for mouse over and button click
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
				    pygame.quit()
				    quit()

				if self.mouse_over_box(pygame.mouse.get_pos(), xPos, yPos1, width, height):
					pygame.draw.rect(self.game.screen, (0, 255, 0), (xPos, yPos1, width, height), 0)
					self.game.screen.blit(label1, (xPos+width/2-10, yPos1+height/2-10))
					mouse_in_box1 = True
				elif self.mouse_over_box(pygame.mouse.get_pos(), xPos, yPos2, width, height):
					pygame.draw.rect(self.game.screen, (0, 255, 0), (xPos, yPos2, width, height), 0)
					self.game.screen.blit(label2, (xPos+width/2-1, yPos2+height/2-10))
					mouse_in_box2 = True

				if pygame.mouse.get_pressed()[0]:
					if mouse_in_box1:
						self.answered = True
						print("said no")
					elif mouse_in_box2:
						self.answered = True
						print("said yes")

			pygame.display.update()



	def mouse_over_box(self, mouse_pos, xPos, yPos, width, height):
		return mouse_pos[0] > xPos and mouse_pos[0] < xPos+width and mouse_pos[1] > yPos and mouse_pos[1] < yPos+height


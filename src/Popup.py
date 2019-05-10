#External Imports
import pygame, os, time, random
from pygame.locals import *

#Local Imports
from LoseScreen import *

class Popup:
	def __init__(self, game, content, correct):
		self.answered = False
		self.correct = correct
		self.game = game
		self.content = content

	def run(self):

		clock = pygame.time.Clock()

		mouse_in_box1 = False
		mouse_in_box2 = False

		width = 100
		height = 50
		xPos = self.game.width/2 - width/2
		yPos1 = self.game.height/2 - height/2 - 3
		yPos2 = self.game.height/2 + height/2 + 3

		render_objects = self.create_render_objects(54)
		label1 = self.game.font.render("NO", False, (255, 255, 255))
		label2 = self.game.font.render("YES", False, (255, 255, 255))

		while not self.answered:

			clock.tick(30)

			self.game.screen.fill((0, 0, 0))

			#display text and answer buttons
			if mouse_in_box1:
				pygame.draw.rect(self.game.screen, (255, 0, 0), (xPos, yPos1, width, height), 0)
				self.game.screen.blit(label1, (xPos+width/2-15, yPos1+height/2-10))
			else:
				pygame.draw.rect(self.game.screen, (100, 100, 100), (xPos, yPos1, width, height), 0)
				self.game.screen.blit(label1, (xPos+width/2-15, yPos1+height/2-10))

			if mouse_in_box2:
				pygame.draw.rect(self.game.screen, (0, 255, 0), (xPos, yPos2, width, height), 0)
				self.game.screen.blit(label2, (xPos+width/2-20, yPos2+height/2-10))
			else:
				pygame.draw.rect(self.game.screen, (100, 100, 100), (xPos, yPos2, width, height), 0)
				self.game.screen.blit(label2, (xPos+width/2-20, yPos2+height/2-10))

			for x in range(1, len(render_objects)):
				self.game.screen.blit(render_objects[x-1], (10, 20*x))

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
						if self.correct == 0:
							print("correct")
						else:
							LoseScreen(self.game, "Oof sorry Theseus, wrong answer :(").run()
							print("incorrect")
					elif mouse_in_box2:
						self.answered = True
						if self.correct == 1:
							print("said yes")
						else:
							LoseScreen(self.game, "Oof sorry Theseus, wrong answer :(").run()
							print("incorrect")

			pygame.display.update()



	def mouse_over_box(self, mouse_pos, xPos, yPos, width, height):
		return mouse_pos[0] > xPos and mouse_pos[0] < xPos+width and mouse_pos[1] > yPos and mouse_pos[1] < yPos+height

	def create_render_objects(self, char_limit=20):
		sentences = []
		render_objects = []
		words = self.content.split(" ")
		while words:
			curr_sentence = ""
			char_count = 0
			for word in words[:]:
				char_count += len(word) + 1
				if char_count <= char_limit:
					curr_sentence += word + " "
					words.remove(word)
					if not words:
						sentences.append(curr_sentence)
						break
				else:
					sentences.append(curr_sentence)
					break
		for sentence in sentences:
			render_objects.append(self.game.font.render(sentence, False, (255, 255, 255)))
		return render_objects


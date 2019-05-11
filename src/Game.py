"""
Author: Nareg A. Megan
Date: 5/8/2019
Classics 28 Project
"""

#External Imports
import pygame, os, time, random
from pygame.locals import *

#Local Imports
from Components import *
from Popup import *
from WinScreen import *
from LoseScreen import *

questions = ["Is the answer to the riddle of the Sphinx in Oedipus the King mankind?",
             "Is it possible to get exactly 4 gallons of water in a 5 gallon jug using only 5 gallon and 3 gallon jugs?", 
             "Is the remainder of dividing 73 by 4, 1?", 
             "Is the probability you roll a 3 with a six sided die increased by 3 times if you roll the die three times?",
             "Is the elephant the largest mammal on the planet?",
             "If you pass the person in second place in a race, are you in first place now?",
             "February during a leap year is the only month containing 28 days.",
             "Dividing 50 by one half gets you 100.",
             "The plural of octopus is octopuses."]

#0 for no 1 for yes
answers = [1, 1, 1, 0, 0, 0, 0, 1, 1]

global riddles

class Game:
    def __init__(self, screen, width, height, game_map, font):
        self.score = 0
        self.over = False
        self.paused = False
        self.font = pygame.font.SysFont('Comic Sans MS', 29)
        self.width = width
        self.height = height
        self.screen = screen
        self.game_map = game_map
        self.font = font

    def run(self):
        begin = time.time()

        player = Player(self.screen, 8, 60, 60, 1, 1, 2)
        tile_map = Map(self.screen, self.game_map, self.width, self.height)
        enemies = Enemies(self.screen, 10, tile_map)

        leftPressed = False
        rightPressed = False
        upPressed = False
        downPressed = False

        clock = pygame.time.Clock()

        while not self.over:
            if not self.paused:
                if player.did_win(tile_map):
                    end = time.time()
                    self.won(end - begin)
                    break

                clock.tick(60)

                #UPDATE POSITIONS

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            rightPressed = True
                        elif event.key == pygame.K_LEFT:
                            leftPressed = True
                        elif event.key == pygame.K_UP:
                            upPressed = True
                        elif event.key == pygame.K_DOWN:
                            downPressed = True
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_RIGHT:
                            rightPressed = False
                        elif event.key == pygame.K_LEFT:
                            leftPressed = False
                        elif event.key == pygame.K_UP:
                            upPressed = False
                        elif event.key == pygame.K_DOWN:
                            downPressed = False

                if leftPressed:
                    player.move_left()
                elif rightPressed:
                    player.move_right()
                if upPressed:
                    player.move_up()
                elif downPressed:
                    player.move_down()

                player.gravity()

                if player.did_collide_with_game_map(tile_map):
                    self.lost("Oof, sorry Theseus, you hit the wall :( Play Again!")
                    break

                enemies.update()
                if player.did_hit_enemies(enemies):
                    self.paused = True

                #RENDER

                self.screen.fill((255, 255, 255))

                tile_map.render()
                player.render()
                enemies.render()


                pygame.display.update()

            else:
                index = random.randint(0, len(questions)-1)
                Popup(self, questions[index], answers[index]).run()

                self.paused = False
                self.screen.fill((255, 255, 255))
                tile_map.render()
                player.render()
                enemies.render()

                pygame.display.update()


    def won(self, elapsed):
        print("Won")
        WinScreen(self, int(elapsed)).run()

    def lost(self, content):
        print("Lost")
        LoseScreen(self, content).run()








"""
Author: Nareg A. Megan
Date: 5/8/2019
Classics 28 Project
"""

#External Imports
import pygame, os, time
from pygame.locals import *

#Local Imports
from Components import *


class Game:
    def __init__(self, screen, width, height, game_map):
        self.score = 0
        self.over = False
        self.font = pygame.font.SysFont('Comic Sans MS', 29)
        self.width = width
        self.height = height
        self.screen = screen
        self.game_map = game_map

    def run(self):
        begin = time.time()

        player = Player(self.screen, 8, 60, 60, 1, 1, 2)
        tile_map = Map(self.screen, self.game_map, self.width, self.height)

        leftPressed = False
        rightPressed = False
        upPressed = False
        downPressed = False

        clock = pygame.time.Clock()

        while not self.over:
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
                if player.did_collide_with_game_map(tile_map):
                    player.move_right()
            elif rightPressed:
                player.move_right()
                if player.did_collide_with_game_map(tile_map):
                    player.move_left()
            if upPressed:
                player.move_up()
                if player.did_collide_with_game_map(tile_map):
                    player.move_down()
            elif downPressed:
                player.move_down()
                if player.did_collide_with_game_map(tile_map):
                    player.move_up()


            #RENDER

            self.screen.fill((255, 255, 255))

            tile_map.render()
            player.render()


            pygame.display.update()

    def won(self, elapsed):
        print("Congrats you won!", "It took you:", int(elapsed), "second(s)!")








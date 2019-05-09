from pygame import draw
import random, math


class Entity:
    def __init__(self, screen, xPos=0, yPos=0, xVel=0, yVel=0, acc=1):
        self.x = xPos
        self.y = yPos
        self.xVel = xVel
        self.yVel = yVel
        self.acc = acc
        self.screen = screen

    def move_right(self):
        self.x += self.acc * self.xVel

    def move_left(self):
        self.x -= self.acc * self.xVel

    def move_up(self):
        self.y -= self.acc * self.yVel

    def move_down(self):
        self.y += self.acc * self.yVel


class Player(Entity):
    def __init__(self, screen, radius, xPos=0, yPos=0, xVel=0, yVel=0, acc=1):
        Entity.__init__(self, screen, xPos, yPos, xVel, yVel, acc)
        self.radius = radius

    def did_collide_with_tile(self, tile):
        inVertical = self.x+self.radius >= tile.x and self.x-self.radius <= tile.x+tile.width
        inHorizontal = self.y+self.radius >= tile.y and self.y-self.radius <= tile.y+tile.height
        return inVertical and inHorizontal

    def did_collide_with_game_map(self, game_map):
        for tile in game_map.tileList:
            if self.did_collide_with_tile(tile):
                return True
        return False
        
    def did_win(self, game_map):
        return self.x > game_map.width or self.x < 0 or self.y > game_map.height or self.y < 0

    def did_hit_enemy(self, enemy):
        return math.sqrt((self.x-enemy.x)**2 + (self.y-enemy.y)**2) <= self.radius + enemy.radius

    def did_hit_enemies(self, enemies):
        for enemy in enemies.enemies:
            if self.did_hit_enemy(enemy):
                enemies.enemies.remove(enemy)
                return True
        return False

    def gravity(self):
        self.y += 1

    def render(self):
        draw.circle(self.screen, (100, 0, 100), (int(self.x), int(self.y)), self.radius, 0)


class Tile(Entity):
    def __init__(self, screen, width, height, xPos, yPos):
        Entity.__init__(self, screen, xPos, yPos)
        self.width = width
        self.height = height

    def render(self):
        draw.rect(self.screen, (0, 0, 0), (int(self.x), int(self.y), self.width, self.height), 0)


class Enemy(Entity):
    def __init__(self, screen, xPos, yPos, radius, xVel=1, yVel=1, acc=1):
        Entity.__init__(self, screen, xPos, yPos, xVel, yVel, acc)
        self.radius = radius

    def render(self):
        draw.circle(self.screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius, 0)


class Enemies:
    def __init__(self, screen, numEnemies, game_map):
        self.screen = screen
        self.game_map = game_map
        self.enemies = []
        self.gen_enemies(numEnemies)

    def add_enemy(self):
        self.enemies.append(Enemy(self.screen, random.randint(10, self.game_map.width-10), 0, 4, 0, random.randint(1, 3)))

    def gen_enemies(self, num):
        enemies = []
        for i in range(num):
            self.add_enemy()

    def update(self):
        for enemy in self.enemies:
            enemy.move_down()
            if enemy.y > self.game_map.height:
                self.enemies.remove(enemy)
                self.add_enemy()

    def render(self):
        for enemy in self.enemies:
            enemy.render()


class Map:
    def __init__(self, screen, game_map, screenWidth, screenHeight):
        self.screen = screen
        self.game_map = game_map 
        self.width = screenWidth
        self.height = screenHeight
        self.tileHeight = screenHeight / len(game_map)
        self.tileWidth = screenWidth / len(game_map[0])
        self.tileList = self.createTileList()

    def render(self):
        for tile in self.tileList:
            tile.render()

    def createTileList(self):
        tilelst = []
        xPos = 0
        for row in self.game_map:
            yPos = 0
            for tile in row:
                if not tile:
                    tilelst.append(Tile(self.screen, self.tileWidth, self.tileHeight ,xPos, yPos))
                yPos += self.tileWidth
            xPos += self.tileHeight
        return tilelst

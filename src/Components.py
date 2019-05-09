from pygame import draw


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
    def __init__(self, screen, xPos, yPos, xVel=1, yVel=1, acc=1):
        Entity.__init__(self, screen, xPos, yPos, xVel, yVel, acc)
        

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

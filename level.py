import pygame
from settings import TILE_SIZE

level = [
"11e111111111111111",
"1        p       1",
"1                1",
"11111111111      1",
"1        11  l   1",
"1     11 11  a   1",
"1     11     b   1",
"1        11      1",
"11111111111      1",
"1  b             1",
"1   11111111111111",
"1   11      c    1",
"1   11           1",
"1   11           1",
"1   ac           1",
"11111111111111   1",
"1           11   1",
"11   1111   11   1",
"1      11   11 l 1",
"1      11   11 l 1",
"1      11        1",
"1      11111111111",
"1                1",
"1                1",
"111111111        1",
"1                1",
"1  111111111111111",
"1                1",
"1                1",
"1111111111111    1",
"1                1",
"1                1",
"111111111111111111"
]

def generateWalls():
    walls = []
    lamps = []
    playerStartX = None
    playerStartY = None
    lampRadius = 90
    isOn = True
    timer = 5
    for y, row in enumerate(level):
        for x, char in enumerate(row):
            if char == "1":
                wall = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                walls.append(wall)
            if char == "p":
                playerStartX = x * TILE_SIZE
                playerStartY = y * TILE_SIZE
            if char == "l":
                lamps.append((x * TILE_SIZE + TILE_SIZE //2, y * TILE_SIZE + TILE_SIZE //2, lampRadius, isOn, timer, 0))
            if char == "a":
                lamps.append((x * TILE_SIZE + TILE_SIZE //2, y * TILE_SIZE + TILE_SIZE //2, lampRadius, isOn, timer + 3, 3))
            if char == "b":
                lamps.append((x * TILE_SIZE + TILE_SIZE //2, y * TILE_SIZE + TILE_SIZE //2, lampRadius, isOn, timer + 4, 2))
            if char == "c":
                lamps.append((x * TILE_SIZE + TILE_SIZE //2, y * TILE_SIZE + TILE_SIZE //2, lampRadius, isOn, timer + 5, 4))
    return walls, playerStartX, playerStartY, lamps
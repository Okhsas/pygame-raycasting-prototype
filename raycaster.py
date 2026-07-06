import math
import pygame
from settings import * 

def rayCasterDDA(player, playerAngle, fov, rayCount, level):

    rayHits = []
    for rayIndex in range(rayCount):
        mapX = int(player.centerx // TILE_SIZE)
        mapY = int(player.centery // TILE_SIZE)

        rayAngle = playerAngle - (fov / 2) + (rayIndex * (fov / rayCount))

        dx = math.cos(math.radians(rayAngle))
        dy = math.sin(math.radians(rayAngle))

        
        if dx < 0:
            stepX = -1
        else:
            stepX = 1
        if dy < 0:
            stepY = -1
        else:
            stepY = 1

        if dx == 0:
            deltaDistanceX = float("inf")
        else:
            deltaDistanceX = abs(1 /dx)

        if dy == 0:
            deltaDistanceY = float("inf")
        else:
            deltaDistanceY = abs(1/dy)

        playerOffSetX = (player.centerx % TILE_SIZE) / TILE_SIZE
        playerOffSetY = (player.centery % TILE_SIZE) / TILE_SIZE

        if stepX > 0:
            sideDistanceX = (1 - playerOffSetX) * deltaDistanceX
        else:
            sideDistanceX = playerOffSetX * deltaDistanceX
        if stepY > 0:
            sideDistanceY = (1 - playerOffSetY) * deltaDistanceY
        else:
            sideDistanceY = playerOffSetY * deltaDistanceY

        side = 0

        for i in range(200):

            if sideDistanceX < sideDistanceY:
                sideDistanceX += deltaDistanceX
                mapX += stepX
                side = 0
            else:
                sideDistanceY += deltaDistanceY
                mapY += stepY
                side = 1

            if mapX < 0 or mapX >= len(level[0]):
                break
            if mapY < 0 or mapY >= len(level):
                break

            if level[mapY][mapX] == "1":

                if side == 0:
                    distance = (sideDistanceX - deltaDistanceX) * TILE_SIZE
                if side == 1:
                    distance = (sideDistanceY - deltaDistanceY) * TILE_SIZE

                if side == 0:
                    wallX = player.centery + distance * dy
                else:
                    wallX = player.centerx + distance * dx

                wallX = wallX % TILE_SIZE

                hitX = player.centerx + distance * dx
                hitY = player.centery + distance * dy

                rayHits.append((distance, rayIndex, rayAngle, side, mapX, mapY, wallX, hitX, hitY))
                break

    return rayHits

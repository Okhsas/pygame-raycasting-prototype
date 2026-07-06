import pygame
import math

def movePlayer(player, keys, walls, playerSpeed, playerAngle):
    playerPositionX = player.x
    playerPositionY = player.y

    dx = math.cos(math.radians(playerAngle))
    dy = math.sin(math.radians(playerAngle))

    if keys[pygame.K_w]:
        player.y += dy * playerSpeed
        player.x += dx * playerSpeed
    if keys[pygame.K_s]:
        player.y -= dy * playerSpeed
        player.x -= dx * playerSpeed
    if keys[pygame.K_d]:
        player.y += dx * playerSpeed
        player.x -= dy * playerSpeed
    if keys[pygame.K_a]:
        player.y -= dx * playerSpeed
        player.x += dy * playerSpeed

    for wall in walls:
        if player.colliderect(wall):
            if keys[pygame.K_d]:
                player.x = playerPositionX
            if keys[pygame.K_a]:
                player.x = playerPositionX
            if keys[pygame.K_w]:
                player.y = playerPositionY
            if keys[pygame.K_s]:
                player.y = playerPositionY
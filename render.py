import pygame
from settings import *
import math

def drawMiniMapWalls(screen, walls):
    for wall in walls:
        miniMapWall = wall.copy()
        miniMapWall.x = wall.x * MINIMAP_SCALE
        miniMapWall.y = wall.y * MINIMAP_SCALE
        miniMapWall.width = wall.width * MINIMAP_SCALE
        miniMapWall.height = wall.height * MINIMAP_SCALE
        pygame.draw.rect(screen, (255, 255, 255), miniMapWall)

def drawPlayerArrow(screen, player, playerAngle):
    playerMiniMap = player.copy()
    playerMiniMap.x = player.x * MINIMAP_SCALE
    playerMiniMap.y = player.y * MINIMAP_SCALE
    playerMiniMap.width = player.width * MINIMAP_SCALE
    playerMiniMap.height = player.height * MINIMAP_SCALE

    arrowLenght = 5

    tipX = playerMiniMap.centerx + math.cos(math.radians(playerAngle)) * arrowLenght
    tipY = playerMiniMap.centery + math.sin(math.radians(playerAngle)) * arrowLenght
    leftX = playerMiniMap.centerx + math.cos(math.radians(playerAngle + 140)) * 4
    leftY = playerMiniMap.centery + math.sin(math.radians(playerAngle + 140)) * 4
    rightX = playerMiniMap.centerx + math.cos(math.radians(playerAngle - 140)) * 4
    rightY = playerMiniMap.centery + math.sin(math.radians(playerAngle - 140)) * 4
    pygame.draw.polygon(screen, (239, 239, 11), [(tipX, tipY), (leftX, leftY), (rightX, rightY)])

def drawMiniMapLamps(screen, lampX, lampY, lampRadius):
    lampMiniMapX = lampX * MINIMAP_SCALE
    lampMiniMapY = lampY * MINIMAP_SCALE
    lampRadius = lampRadius * MINIMAP_SCALE

    pygame.draw.circle(screen, (255, 255, 0), (lampMiniMapX, lampMiniMapY), lampRadius // 2)
    pygame.draw.circle(screen, (25, 255, 0), (lampMiniMapX, lampMiniMapY), 2.5)

def drawWalls(screen, rayHits, wallTexture, lamps):

    for hit in rayHits:
        columWidth = SCREEN_WIDTH / RAY_COUNT

        distance = hit[0]
        rayIndex = hit[1]
        side = hit[3]
        wallx = hit[6]
        hitX = hit[7]
        hitY = hit[8]

        lampBrightness = 0

        for lamp in lamps:

            lampX = lamp[0]
            lampY = lamp[1]
            lampIsOn = lamp[3]
            timer = lamp[4]
            offset = lamp[5]

            currentTime = pygame.time.get_ticks() / 1000

            if int((currentTime + offset) / timer) % 2 == 0:
                lampIsOn = False

            if not lampIsOn:
                continue

            distanceToLamp = math.sqrt(
                (hitX - lampX) ** 2 +
                (hitY - lampY) ** 2
            )

            currentBrightness = max(
                50,
                int(255 - distanceToLamp * 3)
            )

            lampBrightness = max(
                lampBrightness,
                currentBrightness
            )

        correctedDistance = distance

        if correctedDistance <= 0:
            correctedDistance = 0.000001

        columHeight = WALL_SIZE / correctedDistance
        columnY = (SCREEN_HEIGHT / 2) - (columHeight / 2)
        columnX = columWidth * rayIndex

        fogFactor = max(
            0.1,
            1 - correctedDistance / 200
        )

        baseBrightness = 255 * fogFactor

        if side == 1:
            baseBrightness *= 0.7

        brightness = max(
            baseBrightness,
            lampBrightness
        )

        brightness = max(
            0,
            min(255, int(brightness))
        )

        textureX = int(
            wallx * wallTexture.get_width() / TILE_SIZE
        )

        textureColumn = wallTexture.subsurface(
            textureX,
            0,
            1,
            wallTexture.get_height()
        )

        textureColumn = pygame.transform.scale(
            textureColumn,
            (int(columWidth), int(columHeight))
        )

        textureColumn = textureColumn.copy()

        textureColumn.fill(
            (brightness, brightness, brightness),
            special_flags=pygame.BLEND_MULT
        )

        screen.blit(
            textureColumn,
            (columnX, columnY)
        )
import pygame
import math
from settings import MINIMAP_SCALE


def updateLamps(screen, lamps, player):

    playerCaught = False

    for lamp in lamps:

        lampMiniMapX = lamp[0] * MINIMAP_SCALE
        lampMiniMapY = lamp[1] * MINIMAP_SCALE
        lampRadius = lamp[2] * MINIMAP_SCALE

        distanceFromBeingCaught = math.sqrt(
            (player.centerx - lamp[0]) ** 2 +
            (player.centery - lamp[1]) ** 2
        )

        lampRadiusSize = lamp[2]
        lampIsOn = lamp[3]
        timer = lamp[4]
        offset = lamp[5]

        currentTime = pygame.time.get_ticks() / 1000

        if int((currentTime + offset) / timer) % 2 == 0:
            lampIsOn = False

        if lampIsOn and distanceFromBeingCaught < lampRadiusSize // 2:
            playerCaught = True

        if lampIsOn:
            pygame.draw.circle(
                screen,
                (255, 255, 0),
                (lampMiniMapX, lampMiniMapY),
                lampRadius // 2
            )

            pygame.draw.circle(
                screen,
                (25, 255, 0),
                (lampMiniMapX, lampMiniMapY),
                2.5
            )

    return playerCaught
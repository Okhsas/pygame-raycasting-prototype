import pygame
from settings import SCREEN_WIDTH
from settings import SCREEN_HEIGHT

def gameWon(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.SysFont(None, 72)

    text = font.render(
        "YOU ESCAPED!",
        True,
        (255, 255, 0)
    )

    textRect = text.get_rect(
        center=(SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2)
    )

    screen.blit(text, textRect)

    pygame.display.flip()

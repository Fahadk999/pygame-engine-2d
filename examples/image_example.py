import pygame
from pygame_utils.ui.image.Image import Image

pygame.init()

swidth, sheight = 720, 720

screen = pygame.display.set_mode((swidth, sheight), pygame.NOFRAME)
clock = pygame.time.Clock()
running = True
path = "assets/player/player.png"
img = Image(swidth//2, sheight//2, path=path, scale=1.2)

while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    dt = clock.tick(60)

    screen.fill(pygame.Color("cyan"))
    img.Draw(screen)

    pygame.display.flip()

pygame.quit()

import pygame
from pygame_utils.sprites.Shape import Shape

pygame.init()

swidth, sheight = 720, 720

screen = pygame.display.set_mode((swidth, sheight), pygame.NOFRAME)
clock = pygame.time.Clock()
running = True
x, y = swidth//2, sheight//2
circle = Shape.Circle(x-100, y, 80, RB=True)
floor = Shape.Rectangle(x, swidth, swidth, 150, pygame.Color("blue"))
circle.playerCtrler = True

while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    dt = clock.tick(60) / 1000
    circle.Update(dt)
    # floor.Update(dt)
    screen.fill(pygame.Color("cyan"))
    circle.Draw(screen)
    floor.Draw(screen)
    pygame.display.flip()

pygame.quit()

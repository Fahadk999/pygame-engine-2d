import pygame
from pygame_utils.sprites.Shape import Shape

pygame.init()

swidth, sheight = 720, 720

screen = pygame.display.set_mode((swidth, sheight), pygame.NOFRAME)
clock = pygame.time.Clock()
running = True
x, y = swidth//2, sheight//2
circle = Shape.Circle(x-100, y, 80)
rectangle = Shape.Rectangle(x+100, y, 100, 50, pygame.Color("blue"))

while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    dt = clock.tick(60)

    screen.fill(pygame.Color("cyan"))
    circle.Draw(screen)
    rectangle.Draw(screen)
    pygame.display.flip()

pygame.quit()

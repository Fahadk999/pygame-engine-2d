import pygame
from button.buttonStd import Button
pygame.init()

swidth, sheight = 720, 720

screen = pygame.display.set_mode((swidth, sheight), pygame.NOFRAME)
clock = pygame.time.Clock()
running = True
bg = "#2b7aa8"

button = Button(swidth//2, sheight//2)

while running:
    dt = clock.tick(60)/1000 # for time in sec rather then mili sec
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()

    button.hover(pygame.mouse.get_pos())
    screen.fill(bg)
    button.draw(screen)

    pygame.display.flip()

pygame.quit()

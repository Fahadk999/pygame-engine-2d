import pygame
from utility.ui.button.button import Button

pygame.init()

swidth, sheight = 720, 720

screen = pygame.display.set_mode((swidth, sheight), pygame.NOFRAME)
clock = pygame.time.Clock()
running = True
path = "assets/player/player.png"
btn = Button(swidth//2, sheight//2, path=path)

while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    dt = clock.tick(60)

    screen.fill(pygame.Color("lightblue"))
    btn.Draw(screen)

    pygame.display.flip()

pygame.quit()

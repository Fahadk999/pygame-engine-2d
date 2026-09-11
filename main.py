import pygame
from particles.particleEffect import ParticleEffect
pygame.init()

width, height = 720, 720

screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
clock = pygame.time.Clock()
running = True
bg = "#2b7aa8"

effect = ParticleEffect(10, 5)

while running:
    dt = clock.tick(60)/1000 # for time in sec rather then mili sec
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()

    effect.update(dt, width//2, height//2, -30, 5, 140, 1)
    screen.fill(bg)
    effect.draw(screen)

    pygame.display.flip()

pygame.quit()

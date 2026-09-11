import pygame
from particles.particle import Particle
pygame.init()

width, height = 720, 720

screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
clock = pygame.time.Clock()
running = True
bg = "#2b7aa8"

particleGroup = pygame.sprite.Group()
timer = 0
spawnTimer = 50

while running:
    dt = clock.tick(60)
    timer += dt
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    if timer >= spawnTimer:
        particleGroup.add(Particle(width//2, height//2))
        timer = 0

    particleGroup.update(dt)
    screen.fill(bg)
    particleGroup.draw(screen)

    pygame.display.flip()

pygame.quit()

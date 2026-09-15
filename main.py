import pygame
from particles.particleEffect import ParticleEffect
pygame.init()

swidth, sheight = 720, 720

screen = pygame.display.set_mode((swidth, sheight), pygame.NOFRAME)
clock = pygame.time.Clock()
running = True
bg = pygame.Color("#2b7aa8")
c = pygame.Color("#2b7aa8")
d = pygame.Color("red")
effect = ParticleEffect(10)
changed = False

while running:
    dt = clock.tick(60)/1000 # for time in sec rather then mili sec
    events = pygame.event.get()
    mX, mY = pygame.mouse.get_pos()
    effect.initiateParticle(mX, mY, 30)
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mX, mY = pygame.mouse.get_pos()
            effect.initiateParticle(mX, mY, 30)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            if changed == False:
                bg = d
                changed = True
            else:
                bg = c
                changed = False


    keys = pygame.key.get_pressed()

    effect.particleGroup.update(dt)
    screen.fill(bg)
    effect.draw(screen)

    pygame.display.flip()

pygame.quit()

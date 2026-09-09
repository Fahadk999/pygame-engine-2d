import pygame
from button.buttonAnimated import ButtonAnimated
from animationManager.spriteAnimator import AnimatedSprite
pygame.init()

WIDTH, HEIGHT = 720, 720

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
clock = pygame.time.Clock()
running = True
bg = "#2b7aa8"
frames = [f"assets/upgrade_animation/upgrade_{i}.png" for i in range(0, 7)]

button = ButtonAnimated(100, 100, frames)

def changeColor(b):
    global bg
    bg = b
while running:
    dt = clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    mousePos = pygame.mouse.get_pos()
    button.hover(mousePos)
    if button.isHovered:
        button.update(dt)

    button.click(events, changeColor, pygame.Color("blue"))
    
    screen.fill(bg)

    button.draw(screen)

    pygame.display.flip()

pygame.quit()

import pygame
import math
from random import uniform

class Particle(pygame.sprite.Sprite):
    def __init__ (self, x, y, angle):
        super().__init__() 
        self.speed = 140
        self.floatX = x
        self.floatY = y
        w = 8
        self.width, self.height = w, w
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect(center=(int(self.floatX), int(self.floatY)))

        angle = uniform(0, 2*math.pi)
        self.moveX = math.cos(angle)*self.speed
        self.moveY = math.sin(angle)*self.speed

        self.timer = 0
        self.deathTime = 1

    def update (self, dt):
        self.timer += dt
        self.floatX += self.moveX*dt
        self.floatY += self.moveY*dt

        self.rect.centerx = int(self.floatX)
        self.rect.centery = int(self.floatY)

        if self.timer >= self.deathTime:
            self.kill()

    def draw (self, screen):
        screen.blit(self.image, self.rect)


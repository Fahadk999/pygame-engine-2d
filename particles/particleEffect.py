import pygame
from .particle import Particle

# timer is in seconds
class ParticleEffect:
    def __init__ (self, x, y, angle, speed, count):
        self.particleGroup = pygame.sprite.Group()
        self.count = count
        self.angle = angle
        self.timer = 0
        self.spawnTimer = 0.50

    def update (self, dt, x, y):
        self.timer += dt
        if self.timer >= self.spawnTimer:
            self.spawnParticle(swidth, sheight)

        self.particleGroup.update(dt)
        
    def spawnParticle (self, x, y):
        for c in range(0, self.count):
            self.particleGroup.add(Particle(x, y))

    def draw (self, screen):
        self.particleGroup.draw(screen)
         




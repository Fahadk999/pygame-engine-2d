import pygame
from .particle import Particle
from random import uniform

# timer is in seconds
class ParticleEffect:
    def __init__ (self, count, randomTime):
        self.particleGroup = pygame.sprite.Group()
        self.count = count
        self.randomTime = randomTime
        self.timer = 0
        self.maxTime = 0.055
        self.spawnTimer = uniform(0, self.maxTime)

    def spawnParticles (self, dt, x, y, dirAngle, angleOffset=0, speed=140, timeAlive=1):
        self.timer += dt
        if self.timer >= self.spawnTimer:
            if randomTime:
                self.spawnTimer = uniform(0, self.maxTime)
            self.initiateParticle(x, y, dirAngle, angleOffset, speed, timeAlive)
            self.timer = 0
        self.particleGroup.update(dt)

    def initiateParticle (self, x, y, dirAngle, angleOffset, speed, timeAlive):
        for c in range(0, self.count):
            self.particleGroup.add(Particle(x, y, dirAngle, angleOffset, speed, timeAlive))

    def draw (self, screen):
        self.particleGroup.draw(screen)
         




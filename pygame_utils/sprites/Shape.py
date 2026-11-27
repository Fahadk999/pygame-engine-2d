import pygame
from pygame_utils.physics.RigidBody import RigidBody

# later make controler indep of shape class

class Shape:                                                                       # RigibBodyBool 
    def __init__ (self, x, y, width, height, color=pygame.Color("red"), isCircle=False, RB=False):
        self.x, self.y = float(x), float(y)
        self.isCircle = isCircle
        self.color = color
        self.width, self.height = width, height
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.surface.get_rect(center=(self.x, self.y))
        self.speed = 100
        self.rigidBody = RigidBody(self.x, self.y) if RB else None

        # Player controller for wasd
        self.playerCtrler = False
        self.isImg = False # will implement later

        if self.isCircle:
            radius = min(width, height)//2
            center = (self.width//2, self.height//2)
            pygame.draw.circle(self.surface, self.color, center, radius)
        else:
            self.surface.fill(self.color)

    @classmethod
    def Circle (cls, x, y, radius, color=pygame.Color("red"), RB=False):
        diameter = radius*2
        return cls(x, y, diameter, diameter, color, isCircle=True, RB=RB)

    @classmethod
    def Rectangle (cls, x, y, width, height, color=pygame.Color("red"), RB=False):
        return cls(x, y, width, height, color, isCircle=False, RB=RB)

    def Draw (self, screen):
        screen.blit(self.surface, self.rect)

    def Update (self, dt): 
        # Make sure dt/1000 when using aka its seconds not ms
        if self.playerCtrler:
            self.Contoller(dt)
        if self.rigidBody != None:
            self.rect.centery = self.rigidBody.Update(dt)

    def Contoller (self, dt):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if (keys[pygame.K_UP] or  keys[pygame.K_w]):
            dy = -1
        if (keys[pygame.K_DOWN] or  keys[pygame.K_s]):
            dy = 1
        if (keys[pygame.K_LEFT] or  keys[pygame.K_a]):
            dx = -1
        if (keys[pygame.K_RIGHT] or  keys[pygame.K_d]):
            dx = 1

        self.x += dx * self.speed * dt
        self.y += dy * self.speed * dt
        
        self.rect.center = (round(self.x), round(self.y))

import pygame

class Shape: # inhreit rigid body here
    def __init__ (self, x, y, width, height, color=pygame.Color("red"), isCircle=False):
        # player controller for wasd
        self.x, self.y = x, y
        self.isCircle = isCircle
        self.color = color
        self.width, self.height = width, height
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.surface.get_rect(center=(x, y))

        self.playerCtrler = False
        self.isImg = False # will implement later

        if self.isCircle:
            radius = min(width, height)//2
            center = (self.width//2, self.height//2)
            pygame.draw.circle(self.surface, self.color, center, radius)
        else:
            self.surface.fill(self.color)

    @classmethod
    def Circle (cls, x, y, radius, color=pygame.Color("red")):
        diameter = radius*2
        return cls(x, y, diameter, diameter, color, isCircle=True)

    @classmethod
    def Rectangle (cls, x, y, width, height, color=pygame.Color("red")):
        return cls(x, y, width, height, color, isCircle=False)

    def Draw (self, screen):
        screen.blit(self.surface, self.rect)

    def Update (self, dt): # make sure to dt/1000 when using
        if self.playerCtrler:
            self.Contoller(dt)

    def Contoller (self, dt):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP] or  keys[pygame.K_w]):
            # self.rect.x = 0
            pass
        if (keys[pygame.K_DOWN] or  keys[pygame.K_s]):
            pass
        if (keys[pygame.K_LEFT] or  keys[pygame.K_a]):
            pass
        if (keys[pygame.K_RIGHT] or  keys[pygame.K_d]):
            pass
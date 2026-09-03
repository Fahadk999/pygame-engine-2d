import pygame

class BulletStd:
    def __init__(self, x, y, width=100, height=100) -> None:
        self.health = 10
        self.speed = 5
        self.color = pygame.Color("red")

        self.rect = pygame.Rect(x, y, width, height)

    def update (self):
        # self.rect.x += self.speed
        # self.rect.y += self.speed
        pass

    def draw (self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def setAttr (self, attr, val):
        setattr(self, f"{attr}", val)


        
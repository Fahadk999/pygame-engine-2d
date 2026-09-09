import pygame
from .playerStd import PlayerStd

class PlayerSprite (PlayerStd):
    def __init__(self, x, y, path, scale=1):
        super().__init__(x, y)
        self.x, self.y = x, y
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, scale)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw (self, screen):
        screen.blit(self.image, self.rect)
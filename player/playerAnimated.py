import pygame
from .playerStd import PlayerStd
from ..animationManager.spriteAnimator import AnimatedSprite

class PlayerAnimated (PlayerStd):
    def __init__ (self, x, y, frames, scale=1):
        super().__init__(x, y)
        playerAnim = AnimatedSprite(x, y, frames, scale)
        self.spriteGroup = pygame.sprite.Group(playerAnim)
        self.rect = playerAnim.rect

    def update (self, keys, swidth, sheight):
        self.spriteGroup.update()
        self.move(keys, swidth, sheight)

    def draw (self, screen):
        self.spriteGroup.draw(screen)

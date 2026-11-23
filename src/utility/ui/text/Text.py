import pygame
from utility.ui.image.Image import Image
# from abs_path import absPath

class Text:
    def __init__(self, x, y, text, font=None, size=48, color=pygame.Color("white")):
        self.x, self.y = x, y
        self.color = color
        self.text = str(text)
        
        self.font = pygame.font.Font(font, size)
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(center=(self.x, self.y))
        self.glow = False
        self.glowTimer = 0
        self._glowInterval = 300

    def Draw (self, screen):
        screen.blit(self.surface, self.rect)

    def EnableGlow (self):
        self.glow = True

    def SetText (self, text):
        self.surface = self.font.render(str(text), True, self.color)
        self.rect = self.surface.get_rect(center=(self.x, self.y))

    def UpdatePos (self, newX, newY):
        self.rect = self.surface.get_rect(center=(newX, newY))

    # will fix later, make a wait when glow and basic color, avoid filckering
    def MakeGlow (self, dt, glowColor="yellow"):
        if self.glow:
            if self.glowTimer <= self._glowInterval:
                self.glowTimer += dt
                self.color = pygame.Color(glowColor)
                self.surface = self.font.render(self.text, True, self.color)
            else:
                self.glowTimer = 0
                self.color = pygame.Color("white")
                self.surface = self.font.render(self.text, True, self.color)

    @property
    def glowInterval (self):
        return self._glowInterval

    @glowInterval.setter
    def glowInterval (self, val):
        if val <= 0:
            raise ValueError("Glow Interval cant be 0 or Negative!!")

        self._glowInterval = val

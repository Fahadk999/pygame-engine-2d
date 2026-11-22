import pygame
# from abs_path import absPath
# rename this file to Text.py

class Text:
    def __init__(self, text, posX, posY, font=None, size=48, color=pygame.Color("white")):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.text = str(text)
        
        self.font = pygame.font.Font(font, size)
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(center=(self.posX, self.posY))
        self.glow = False
        self.glowTimer = 0
        self._glowInterval = 300

    def Draw (self, screen):
        screen.blit(self.surface, self.rect)
        pygame.draw.rect(screen, "red", self.rect, width=2)

    def EnableGlow (self):
        self.glow = True

    def SetText (self, text):
        self.surface = self.font.render(str(text), True, self.color)
        self.rect = self.surface.get_rect(center=(self.posX, self.posY))

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

import pygame
from ..text.Text import Text
from ..image.Image import Image

class Button:
    def __init__ (
            self, x, y,
            width=None, height=None,
            text="Button", size=30, padding = 0,
            path=None
        ):
        self.x, self.y = x, y
        # if width and height = none auto take height
        self.width, self.height = width, height
        self.isImage = False

        self.baseColor = pygame.Color("red")
        self.hoverColor = pygame.Color("black")
        self.color = self.baseColor
        self.text = text
        self.path = path
        self.defaultScale = 1.0
        self.scale = 1.0
        self.scaleRate = 0.04
        self.maxScale = 1.2
        self._padding = padding
        
        self.text = Text(self.x, self.y, f"{text}", size=size)
        if self.path == None:
            if width == None and height == None:
                self.width = self.text.rect.width
                self.height = self.text.rect.height
            self.image = pygame.Surface((self.width + padding, self.height + padding))
            self.image.fill((self.color))
            self.rect = self.image.get_rect(center=(self.x, self.y))
        else:
            self.image = Image.GetImage(path) 
            self.rect = Image.GetImageRect(x, y, self.image)
            self.isImage = True # for hover and click color switch

        self.origImage = self.image.copy() # for scaling proper
        # Text of Button
        
        self.isHovered = False
        self.colorChange = True

    def Draw (self, screen):
        screen.blit(self.image, self.rect)
        self.text.Draw(screen)
    
    def Hover (self):
        pos = pygame.mouse.get_pos()
        self.isHovered = self.rect.collidepoint(pos)
        self.ChangeScale()

    # def ChangeColor (self): # not used any where btw
    #     if self.colorChange and self.isHovered:
    #         self.color = self.hoverColor
    #         self.origImage.fill((self.color))
    #     else:
    #         self.color = self.baseColor
    #         self.origImage.fill((self.color))

    def Click (self, events, function, *args):
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if self.isHovered:
                    self.origImage.fill(pygame.Color("white"))
                    return function(*args)
            elif e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                self.origImage.fill(self.baseColor)
                return
   
    def ChangeScale (self):
        # add time for scaling
        if self.isHovered:
            if self.scale < self.maxScale:
                self.scale += self.scaleRate
                self.scale = self.maxScale if self.scale > self.maxScale else self.scale
        else:
            if self.scale > self.defaultScale: 
                self.scale -= self.scaleRate
                self.scale = self.defaultScale if self.scale < self.defaultScale else self.scale

        self.image = pygame.transform.scale_by(self.origImage, self.scale)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    @property
    def padding (self):
        return self.padding
    @padding.setter
    def padding (self, val):
        if val < 0:
            raise ValueError("Padding can not be 0 or smaller")
        self._padding = val

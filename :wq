import pygame
#fix path for your text file
from ..text.Text import Text
from ..image.Image import Image

#transitno animatin is left make it so that it take transition time
class Button:
    def __init__ (
            self, x, y,
            width=100, height=100,
            text="Button", size=30,
            path=None
        ):
        self.x, self.y = x, y
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
        self._padding = 0
        
        if self.path == None:
            self.image = pygame.Surface((width, height))
            self.image.fill((self.color))
            self.rect = self.image.get_rect(center=(self.x, self.y))
        else:
            self.image = Image.GetImage(path) 
            self.rect = Image.GetImageRect(x, y, self.image)
            self.isImage = True

        # Text of Button
        self.text = Text(self.rect.centerx, self.rect.centery, f"{text}", size=size)
        
        self.isHovered = False
        self.scaled = False
        self.colorChange = True

    def Draw (self, screen):
        screen.blit(self.image, self.rect)
        self.text.Draw(screen)
    
    def Hover (self):
        pos = pygame.mouse.get_pos()
        self.isHovered = self.rect.collidepoint(pos)
        self.ChangeScale()

    def ChangeColor (self):
        if self.colorChange and self.isHovered:
            self.color = self.hoverColor
            self.image.fill((self.color))
        else:
            self.color = self.baseColor
            self.image.fill((self.color))

    def Click (self, events, function, *args) -> Any:
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if self.isHovered:
                    return function(*args)
   
    def ChangeScale (self):
        if self.isHovered:
            if self.scale <= self.maxScale:
                self.scale += self.scaleRate
                # newScale = self.maxScale if self.scale > self.maxScale else self.scale
                self.image = pygame.transform.scale_by(self.image, self.scale)
                self.scaled = True
        else:
            # not returning to original size
            if self.scale >= self.defaultScale: # <- remove self.scaled bool
                self.scale -= self.scaleRate
                # newScale = 0 if self.scale <= 0 else 1/self.scale 
                self.image = pygame.transform.scale_by(self.image, self.scale)
                self.scaled = False

        self.rect = self.image.get_rect(center=(self.x, self.y))

    @property
    def padding (self):
        return self.padding
    @padding.setter
    def padding (self, val):
        if val < 0:
            raise ValueError("Padding can not be 0 or smaller")
        self._padding = val

# whiel hover size++ to limit, !hover size-- to limit        
# for practice add 0.25 to size

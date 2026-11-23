import pygame
#fix path for your text file
from ..text.Text import Text
from ..image.Image import Image

# if w and h are none then get them from text and padding
# if path thne load img else use normal surface
# first not path
# img bool for hover
class Button:
    def __init__ (
            self, x, y,
            width=100, height=100,
            text="Button", size=30,
            path=None
        ):
        self.x, self.y = x, y
        self.width, self.height = width, height

        self.baseColor = pygame.Color("red")
        self.hoverColor = pygame.Color("black")
        self.color = self.baseColor
        self.text = text
        self.path = path;
        
        if self.path == None:
            self.image = pygame.Surface((width, height))
            self.image.fill((self.color))
            self.rect = self.image.get_rect(center=(self.x, self.y))
        else:
            self.image = Image(x, y, path)
            self.rect = self.image.rect

        # Text of Button
        self.text = Text(self.rect.centerx, self.rect.centery, f"{text}", size=size)
        
        self.isHovered = False
        self.scaleChange = True
        self.colorChange = True

        self.hoverWidth = width+10
        self.hoverHeight = height+10

    def Draw (self, screen):
        screen.blit(self.image.image, self.rect)
        self.text.Draw(screen)

    def Hover (self):
        pos = pygame.mouse.get_pos()
        self.isHovered = self.rect.collidepoint(pos)
        self.changeColor()
        self.changeScale()

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
        if self.scaleChange:
            if self.isHovered:
                self.image = pygame.transform.scale(self.image, (self.hoverWidth, self.hoverHeight))
            else:
                self.image = pygame.transform.scale(self.image, (self.width, self.height))

            self.rect = self.image.get_rect(center=(self.x, self.y))

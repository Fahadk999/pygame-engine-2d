import pygame

class ButtonStd:
    def __init__ (self, x, y, width=100, height=50):
        self.x, self.y = x, y
        self.width, self.height = width, height

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (self.x, self.y)

        self.baseColor = pygame.Color("red")
        self.hoverColor = pygame.Color("orange")
        self.color = self.baseColor

        self.isHovered = False
        self.scaleChange = True
        self.colorChange = True

        self.w = width+10
        self.h = height+5

    def draw (self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def hover (self, pos):
        self.isHovered = self.rect.collidepoint(pos)
        self.changeColor()
        self.changeScale()

    def changeColor (self):
        if self.colorChange and self.isHovered:
            self.color = self.hoverColor
        else:
            self.color = self.baseColor

    def click (self, events, function, *args) -> Any:
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if self.isHovered:
                    return function(*args)
   
    def changeScale (self):
        if self.scaleChange:
            if self.isHovered:
                self.rect.width = self.w 
                self.rect.height = self.h
            else:
                self.rect.width = self.width
                self.rect.height = self.height

            self.rect.center = (self.x, self.y)
    

        

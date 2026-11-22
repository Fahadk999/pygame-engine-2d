import pygame

class Image:
    def __init__ (self, x, y, path, scale=1.0):
        self.path = path
        self.x, self.y = x, y

        self.rawImage = pygame.image.load(self.path).convert_alpha()
        self.tightBounds = self.rawImage.get_bounding_rect()
        self.croppedImage = self.rawImage.subsurface(self.tightBounds).copy()
        
        if scale != 1.0:
            self.image = pygame.transform.scale_by(
                    self.croppedImage, scale
                    )
        else:
            self.image = self.croppedImage

        self.rect = self.image.get_rect(center=(x, y))

    def Draw (self, screen):
        screen.blit(self.image, self.rect)

    def Resize (self, newScale):
        self.image = pygame.transform.scale_by(
                self.croppedImage, scale
                )
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def SetPos (self, x, y):
        self.rect.center = (x, y)


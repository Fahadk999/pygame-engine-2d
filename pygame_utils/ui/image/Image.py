import pygame

class Image:
    def __init__ (self, x, y, path, scale=1.0):
        self.path = path
        self.x, self.y = x, y

        self.image = self.GetImage(path, scale)
        self.origImage = self.image.copy()
        self.rect = self.image.get_rect(center=(x, y))

    @classmethod
    def GetImage (cls, path, scale=1.0):
        rawImage = pygame.image.load(path).convert_alpha()
        tightBounds = rawImage.get_bounding_rect()
        croppedImage = rawImage.subsurface(tightBounds).copy()
        if scale != 1.0:
            image = pygame.transform.scale_by(
                    croppedImage, scale
                    )
        else:
            image = croppedImage

        return image

    @classmethod
    def GetImageRect (cls, x, y, image):
        return image.get_rect(center=(x, y)) 

    def Draw (self, screen):
        screen.blit(self.image, self.rect)

    def Resize (self, newScale):
        self.image = pygame.transform.scale_by(
                self.origImage, newScale
                )
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def SetPos (self, x, y):
        self.rect.center = (x, y)


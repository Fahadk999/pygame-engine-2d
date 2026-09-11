import pygame
# from abs_path import absPath

class LoadImage:
    def __init__(self, x, y, path, scale=1.0):
        self.path = path
        self.rawImage = pygame.image.load(self.path).convert_alpha()
        tightBounds = self.rawImage.get_bounding_rect()
        croppedImage = self.rawImage.subsurface(tightBounds).copy()

        if scale != 1.0:
            self.image = pygame.transform.scale_by(
                croppedImage, scale
            )
        else:
            self.image = croppedImage

        self.rect = self.image.get_rect(center=(x, y))

        # For Idle Y aka up down idle
        self.idleYTimer = 0
        self.idleYUpDir = True
        self.origY = self.rect.y
        self.maxY = self.rect.y+5
        self.minY = self.rect.y-5

    def draw (self, screen):
        screen.blit(self.image, self.rect)

    def resize (self, width, height):
        prevCenter = self.rect.center
        self.image = pygame.transform.scale(
            self.rawImage, (width, height)
        )
        self.rect = self.image.get_rect(center=prevCenter)


    def idleAnimationY (self, dt, speed, interval):
        self.idleYTimer += dt
        if self.idleYTimer >= interval:
            if self.idleYUpDir: # if true
                self.rect.y += -speed
            else:
                self.rect.y += speed
            self.idleYTimer -= interval
        if abs(speed) == speed:
            if self.rect.y >= self.maxY:
                self.idleYUpDir = True
            if self.rect.y <= self.minY:
                self.idleYUpDir = False
        else:
            if self.rect.y >= self.maxY:
                self.idleYUpDir = False
            if self.rect.y <= self.minY:
                self.idleYUpDir = True

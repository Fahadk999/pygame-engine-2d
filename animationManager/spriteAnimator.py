import pygame

class AnimatedSprite (pygame.sprite.Sprite):
    def __init__ (self, x, y, imgPaths, scale=1.0):
        super().__init__()
        self.frames = []
        for path in imgPaths:
            img = pygame.image.load(path).convert_alpha()
            if scale != 1.0:
                newSize = (
                    int(img.get_width() * scale),
                    int(img.get_height() * scale)
                )
                img = pygame.transform.scale(img, newSize)
            self.frames.append(img)

        self.currFrame = 0
        self.animationSpeed = 0.15

        self.image = self.frames[int(self.currFrame)]
        self.rect = self.image.get_rect(center=(x, y))

    def update (self):
        self.currFrame += self.animationSpeed

        if self.currFrame >= len(self.frames):
            self.currFrame = 0

        self.image = self.frames[int(self.currFrame)]

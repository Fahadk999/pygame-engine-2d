import pygame 
from ui.imageloader import LoadImage

class PlayerStd(pygame.sprite.Sprite):
    def __init__(self, x, y, path="", width=100, height=100, scale:float=1.0):
        self.x, self.y = x, y
        self.speed = 5
        self.color = pygame.Color("white")
        if path == "":
            self.image = pygame.Surface((width, height))
            self.image.fill(self.color)
            newRect = self.image.get_rect(center=(x,y))
        else:
            self.rawImage = LoadImage(x, y, path, scale)
            self.image = self.rawImage.image
            newRect = self.rawImage.rect
        self.rect = newRect

    def update (self, keys, swidth, sheight):
        self.move(keys, swidth, sheight)

    def move (self, keys, swidth, sheight):
        dx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += self.speed

        dy = 0
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy += self.speed

        self.rect.x += dx
        self.rect.y += dy

        half_width = self.rect.width / 2
        half_height = self.rect.height / 2
        self.rect.left = max(-half_width, self.rect.left)
        self.rect.right = min(swidth + half_width, self.rect.right)
        self.rect.top = max(-half_height, self.rect.top)
        self.rect.bottom = min(sheight + half_height, self.rect.bottom)

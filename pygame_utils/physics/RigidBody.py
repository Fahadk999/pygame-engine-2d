import pygame

# maybe return velocity
class RigidBody:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.mass = 1
        self.gravity = 10
        # accenleration

    def Update (self, dt) -> float:
        # fix this shi
        self.y += self.gravity * self.mass * dt
        return self.y

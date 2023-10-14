from pygame import Rect

from calcs import Point,Vector
from parameters import *
import random

class Particle(Point):
    def __init__(self, x, y, color=None):
        super().__init__(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = Vector(0, 0)
        self.radius = 5
        self.color = color
        self.collisions = 0

    def collides_with(self, other):
        return self.distance(other) < self.radius + other.radius

    def resolve_collision(self, other):
        if not self.collides_with(other):
            return

        dx = self.x - other.x
        dy = self.y - other.y

        distance = self.distance(other)
        overlap = 0.5 * (distance - self.radius - other.radius)  # How much the circles overlap

        # Resolve the positional overlap first
        separation_vector = Vector(dx, dy).normalized()
        self.move(separation_vector.multiplied_by(-overlap))
        other.move(separation_vector.multiplied_by(overlap))

        # Now handle the velocity part (elastic collision)
        rsq = (dx*dx) + (dy*dy)
        dvx = self.velocity.h - other.velocity.h
        dvy = self.velocity.v - other.velocity.v
        b = (dx*dvx) + (dy*dvy)
        if rsq == 0:
            return
        delvx = (-b * dx) / rsq
        delvy = (-b * dy) / rsq

        self.velocity.h += delvx
        self.velocity.v += delvy
        other.velocity.h -= delvx
        other.velocity.v -= delvy

        self.collisions += 1

    def boundary(self):
        push_back = 1  # Push the particle slightly away from the boundary after bouncing
        if self.x >= WIDTH - self.radius:
            self.x = WIDTH - self.radius - push_back
            self.velocity.h = -abs(self.velocity.h)
        if self.x <= self.radius:
            self.x = self.radius + push_back
            self.velocity.h = abs(self.velocity.h)
        if self.y >= HEIGHT - self.radius:
            self.y = HEIGHT - self.radius - push_back
            self.velocity.v = -abs(self.velocity.v)
        if self.y <= self.radius:
            self.y = self.radius + push_back
            self.velocity.v = abs(self.velocity.v)      

    def update(self):
        self.velocity.multiply(DAMPING)
        self.move(self.velocity)
        self.boundary()

    def draw(self,screen):
        screen.draw.circle((self.x, self.y), self.radius, self.color)

class Square(Point):
    def __init__(self, x, y, color=None):
        super().__init__(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = Vector(0, 0)
        self.size = 10
        self.color = color
        self.collisions = 0

    def collides_with(self, other):
        return (other.x < self.x + self.size and other.x + other.size > self.x) and (other.y < self.y + self.size and other.y + other.size > self.y)

    def resolve_collision(self, other):
        if not self.collides_with(other):
            return

        overlap_x, overlap_y = self.calculate_overlap(other)

        if overlap_x < overlap_y:
            self.resolve_x_collision(other, overlap_x)
        else:
            self.resolve_y_collision(other, overlap_y)

        self.collisions += 1

    def calculate_overlap(self, other):
        overlap_x = self.size + other.size - abs(self.x - other.x)
        overlap_y = self.size + other.size - abs(self.y - other.y)
        return overlap_x, overlap_y

    def resolve_x_collision(self, other, overlap_x):
        if self.x < other.x:
            other.x = self.x + self.size
        else:
            self.x = other.x + other.size
        self.switch_horizontal_velocity(other)

    def resolve_y_collision(self, other, overlap_y):
        if self.y < other.y:
            other.y = self.y + self.size
        else:
            self.y = other.y + other.size
        self.switch_vertical_velocity(other)

    def switch_horizontal_velocity(self, other):
        temp_velocity = self.velocity.h
        self.velocity.h = other.velocity.h
        other.velocity.h = temp_velocity

    def switch_vertical_velocity(self, other):
        temp_velocity = self.velocity.v
        self.velocity.v = other.velocity.v
        other.velocity.v = temp_velocity

    def boundary(self):
        push_back = 1  # Push the particle slightly away from the boundary after bouncing
        if self.x >= WIDTH - self.size:
            self.x = WIDTH - self.size - push_back
            self.velocity.h = -abs(self.velocity.h)
        if self.x <= 0:
            self.x = 0 + push_back
            self.velocity.h = abs(self.velocity.h)
        if self.y >= HEIGHT - self.size:
            self.y = HEIGHT - self.size - push_back
            self.velocity.v = -abs(self.velocity.v)
        if self.y <= 0:
            self.y = 0 + push_back
            self.velocity.v = abs(self.velocity.v)
        
    def update(self):
        self.velocity.multiply(DAMPING)
        self.move(self.velocity)
        self.boundary()

    def draw(self,screen):
        screen.draw.rect(Rect((self.x,self.y),(self.size,self.size)),'black')
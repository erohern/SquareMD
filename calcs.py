class Vector:
    def __init__(self, h, v):
        self.h = h
        self.v = v

    def add(self, vector):
        self.h += vector.h
        self.v += vector.v

    def subtract(self, vector):
        self.h -= vector.h
        self.v -= vector.v

    def multiply(self, scalar):
        self.h *= scalar
        self.v *= scalar

    def multiplied_by(self, scalar):
        return Vector(self.h * scalar, self.v * scalar)

    def divide(self, scalar):
        self.h /= scalar
        self.v /= scalar
    
    def divide_by(self,int):
        return Vector((self.h * int),(self.v * int))

    def length(self):
        return (self.h**2 + self.v**2)**0.5

    def normalize(self):
        length = self.length()
        self.h /= length+.00000001
        self.v /= length+.00000001

    def normalized(self):
        len = self.length()
        if len == 0:
            return Vector(0,0)  # Default zero vector
        return Vector(self.h/len, self.v/len)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getpos(self):
        return self.x, self.y

    def distance(self, other):
        ox, oy = other.getpos()
        return ((self.x - ox)**2 + (self.y - oy)**2)**0.5

    def move(self, vector):
        self.x += vector.h
        self.y += vector.v

    def makeVectorTo(self, other):
        dx = other.x + self.x
        dy = other.y + self.y
        v = Vector(dx, dy)
        return v
    
    def makeVectorTo2(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        v = Vector(dx, dy)
        return v
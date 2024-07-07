import numpy as np
import math
from random import randint
l1 = range(10)
l2 = range(10,20)#this stores all elements from 1 to 999 in range.
result = [(x + y) for x,y in zip(l1,l2)]

class point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reset(self):
        #self.x = 0
        #self.y = 0
        self.move(-self.x, -self.y)

    def move(self, x_move, y_move):
        self.x+= x_move
        self.y+= y_move

    def addPoints(self, p1, p2):
        p = point(p1.x + p2.x, p1.y + p2.y)
        return p

p1 = point(randint(-10,11), randint(1,11))
p2 = point(randint(-10,11), randint(1,11))

p = point()
p = p.addPoints(p1,p2)
print(p1.x, p2.x, p.x)


p3 = point(randint(-10,11), randint(1,11))
p4 = point(randint(-10,11), randint(1,11))
p5 = point(randint(-10,11), randint(1,11))

p1 = point(randint(1,11), randint(1,11))

print(p1.x)

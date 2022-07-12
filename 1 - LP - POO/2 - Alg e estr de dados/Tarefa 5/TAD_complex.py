#
#


from cmath import sqrt
from turtle import ycor


class Complx:
    def __init__(self, x, y) -> complex:
       self = x + y*sqrt(-1) 
       self.x = x
       self.y = y
        
n1 = Complx(1,3)
print(n1)

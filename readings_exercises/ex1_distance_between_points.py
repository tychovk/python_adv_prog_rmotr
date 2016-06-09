'''
http://www.greenteapress.com/thinkpython/html/thinkpython016.html
Write a function called distance_between_points that takes two Points as 
arguments and returns the distance between them.
'''
import math

class CoordSet:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance_between_points(point_1, point_2):
    '''receives points as attributes'''
    x_diff = point_1.x - point_2.x
    y_diff = point_1.y - point_2.y
    return math.sqrt(x_diff ** 2 + y_diff ** 2)
    
point_1 = CoordSet(5, 3)
point_2 = CoordSet(7, 5)    
    
print (distance_between_points(point_1, point_2))
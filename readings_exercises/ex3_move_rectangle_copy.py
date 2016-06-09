"""
http://www.greenteapress.com/thinkpython/html/thinkpython016.html
Exercise 3  
Write a version of move_rectangle that creates and returns a new Rectangle instead of modifying the old one.

"""
import copy

class CoordsSet:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    
def copy_rectangle_to(rect, new_x, new_y):
    rect_copy = copy.deepcopy(rect)
    rect_copy.corner.x = new_x
    rect_copy.corner.y = new_y
    return rect_copy
    
    
    
box1 = Rectangle(4, 5)
box1.corner = CoordsSet(5, 6)

box2 = copy_rectangle_to(box1, 2, 3)

print (box1.corner.x)
print (box1.corner.y)

print ("box2")
print (box2.corner.x)
print (box2.corner.y)
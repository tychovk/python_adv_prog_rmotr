
class CoordsSet:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

        
box = Rectangle(100, 200)
box.corner = CoordsSet(0,0)

print (box.corner.x, box.corner.y)

move_rectangle(box, 5, 6)

print (box.corner.x, box.corner.y)


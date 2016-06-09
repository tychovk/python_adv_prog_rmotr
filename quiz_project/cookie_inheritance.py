COLORS = {
    'blue': 'ab2399',
    'red': 'ba3224'
}

class Food:
    def __init__(self, color):
        self.color = COLORS[color.lower()]
        
        
    @classmethod   
    def create_instances(cls, color, instances):
        the_food = cls(color)
        foods = [the_food for i in range(instances)]
        return foods

class Cookie(Food):
    def __init__(self, color, number_of_buttons=2):
        super().__init__(color)
        self.number_of_buttons = number_of_buttons 

        



        
class Apple(Food):
    pass


cookies = Cookie.create_instances("blue", instances=5)
apples = Apple.create_instances("blue", instances=5)
print (cookies)
print (apples)

    
    
c = Cookie(color="Blue", number_of_buttons=2)

print("Cookie's color: {}".format(c.color))

a = Apple(color="Red")
print("Apple's color: {}".format(a.color))



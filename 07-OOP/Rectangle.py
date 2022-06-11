

class Rectangle:

    def __init__(self, length, width):
        self.length = length 
        self.width = width 


class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width) # we use the super method to copy the code in the rectangle init, so we don't need to write twice

    def area(self):
        return self.length * self.width

    
class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height 

    def volume(self):
        return self.length * self.width * self.height

    
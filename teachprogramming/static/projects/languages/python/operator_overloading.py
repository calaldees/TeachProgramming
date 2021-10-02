
class Circle():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def __repr__(self):
        return f"Circle({self.x=}, {self.y=}, {self.radius=})"
    def __str__(self):
        return repr(self)
    def __add__(self, other):
        if (isinstance(other, Circle)):
            return Circle(
                x = (self.x + other.x)/2,
                y = (self.y + other.y)/2,
                radius = self.radius + other.radius,
            )
        if (isinstance(other, (int, float))):
            return Circle(
                x = self.x,
                y = self.y,
                radius = self.radius + other
            )
        raise NotImplementedError(f"Unable to add '{other}'")



class Rectangle():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def __repr__(self):
        return f"Rectangle({self.x1=}, {self.y1=}, {self.x2=}, {self.y2=})"
    def __str__(self):
        return repr(self)
    def __add__(self, other):
        # adding another rectangle should create a new rectable that encompasses both rectangles?
        # hint there are two built in functions that may help - one of them is min - https://docs.python.org/3/library/functions.html
        raise NotImplementedError(f"Unable to add '{other}'")
    #def __???__(self, other):
        # Can you implement another operator? can you make 'subtract' remove from the width/height of the rectangle?

if __name__ == "__main__":
    print(
        Circle(5,5,5) + Circle(2,2,5)
    )
    Circle(1,2,3) + 5
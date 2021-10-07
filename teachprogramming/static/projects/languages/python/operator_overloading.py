"""
This python exercise is a example of:
 - Operator Overloading
 - Doctests
"""

# Predict what this program should print (preferably discuss your idea with another person)
# then run it
# Can you describe why this has happened?
# Is this good? or bad?

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

if __name__ == "__main__":
    print(
        Circle(5,5,5) + Circle(2,2,5)
    )
    print(
        Circle(1,2,3) + 5
    )


# ------------------------------------------------------------------------------

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
        """
        This is a doctest - you can run this from the command line with
        python3 -m doctest -o ELLIPSIS NAME_OF_FILE.py

        >>> r1 = Rectangle(0,0,10,10)
        >>> r2 = Rectangle(5,5,20,20)

        >>> r1 + "bob"
        Traceback (most recent call last):
        NotImplementedError: Unable to add ...

        >>> r1 + r2
        Rectangle(self.x1=0, self.y1=0, self.x2=20, self.y2=20)

        >>> r2 + r1
        Rectangle(self.x1=0, self.y1=0, self.x2=20, self.y2=20)

        >>> r1 + 1
        Rectangle(self.x1=0, self.y1=0, self.x2=11, self.y2=11)
        """
        # Part 1: Implement the `+` operator
        # hint there are two built in functions that may help - one of them is min - https://docs.python.org/3/library/functions.html
        raise NotImplementedError(f"Unable to add '{other}'")

    # Part 2: Implement another operator
    #def __???__(self, other):
        # Can you implement another operator? can you make 'subtract' remove from the width/height of the rectangle?
        # https://docs.python.org/3/library/operator.html
    
    # Part 3: Identify other operators that can be overloaded
    # https://docs.python.org/3/library/operator.html
    # Is operator overloading good? or bad? why?

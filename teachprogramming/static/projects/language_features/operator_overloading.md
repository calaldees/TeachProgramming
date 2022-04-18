Operator Overloading
--------------------

python
```python
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
        if isinstance(other, Circle):
            return Circle(
                x = (self.x + other.x)/2,
                y = (self.y + other.y)/2,
                radius = self.radius + other.radius,
            )
        if isinstance(other, (int, float)):
            return Circle(
                x = self.x,
                y = self.y,
                radius = self.radius + other
            )
        raise NotImplementedError(f"Unable to add '{other}'")

if __name__ == "__main__":
    print(Circle(5,5,5) + Circle(2,2,5))
    print(Circle(1,2,3) + 5)
```

csharp
```csharp
class Circle {
    double x;
    double y;
    double radius;

    public Circle(double x, double y, double radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    override
    public String ToString() {
        return $@"Circle(x={x}, y={y}, radius={radius})";
    }

    public static Circle operator +(Circle a, Circle b) {
        return new Circle(x: (a.x + b.x)/2, y: (a.y + b.y)/2, radius: a.radius + b.radius);
    }

    public static Circle operator +(Circle a, int r) {
        return new Circle(x: a.x, y: a.y, radius: a.radius + r);
    }
}

Console.WriteLine(new Circle(5,5,5) + new Circle(2,2,5));
Console.WriteLine(new Circle(1,2,3) + 5);
```

python
```python
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
        python3 -m doctest -v -o ELLIPSIS NAME_OF_FILE.py

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
        # hint use the circle example above for ideas
        # hint there are two built in functions that may help - one of them is `max()` - https://docs.python.org/3/library/functions.html#max
        raise NotImplementedError(f"Unable to add '{other}'")

    # Part 2: Implement another operator
    # def __???__(self, other):
        # Can you implement another operator? can you make 'subtract' remove from the width/height of the rectangle?
        # https://docs.python.org/3/library/operator.html
    
    # Part 3: Identify other operators that can be overloaded
    # https://docs.python.org/3/library/operator.html
    # Is operator overloading good? or bad? why?
```

csharp
```csharp
class Rectangle {
    int x1;
    int y1;
    int x2;
    int y2;

    public Rectangle(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }

    public override String ToString() => $"Rectangle(x1:{x1}, y1:{y1}, x2:{x2}, y2:{y2})";
    public override int GetHashCode() => x1 ^ y1 ^ x2 ^ y2;
    public override bool Equals(object obj) => GetHashCode()==obj.GetHashCode();  // Quick Hack

    public static Rectangle operator +(Rectangle a, Rectangle b) {
        throw new NotImplementedException("Complete this + operator");
    }
    public static Rectangle operator +(Rectangle a, int b) {
        throw new NotImplementedException("Complete this + operator");
    }
}


var r1 = new Rectangle(0,0,10,10);
var r2 = new Rectangle(5,5,20,20);

AssertIsEqual(r1 + r2, new Rectangle(0, 0, 20, 20));
AssertIsEqual(r1 + 1, new Rectangle(0, 0, 11, 11));
```

### Documentation
* https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
* https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/operator-overloading


I've used this for TimeLine objects
https://github.com/calaldees/libs/blob/eeddc0f8fdad48f7595c56a2ed1b4ae23ab14b96/python3/calaldees/animation/timeline.py#L211



* [4 Reasons Why Java doesn't support Operator Overloading](https://javarevisited.blogspot.com/2011/08/why-java-does-not-support-operator.html)

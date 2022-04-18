Reference Equality by default
-----------------------------

* _Predict_ what this program should print (preferably discuss your idea with another person)
* then _run_ it
* Can you describe why this has happened?
* Is this good? or bad?


java
```java
import java.awt.Point;
class Main {
  public static void main(String[] args) {
    Point p1 = new Point(1,1);
    Point p2 = new Point(1,1);
    System.out.println(p1 == p2);
  }
}
```

csharp
```csharp
class Point {
    int a;
    int b;
    public Point(int a, int b) {
        this.a = a;
        this.b = b;
    }
}

Point p1 = new Point(1,1);
Point p2 = new Point(1,1);
Console.WriteLine(p1 == p2);
```

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
* `==` is reference equality
* StackOverflow: [What is the proper way to implement a robust equals() and hashCode() method in an inheritance hierarchy?](https://stackoverflow.com/a/53291782/3356840)

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
* `==` is reference equality
* [How to define value equality for a class or struct (C# Programming Guide)](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/statements-expressions-operators/how-to-define-value-equality-for-a-type)


```javascript
1 == "1"
1 === "1"
```
`==` Implicit conversion


List/array equality?
-------------------
A false carryover-concept
Which languages perform deep object content comparisons by default

```python
aa = [1,2,3]
bb = [1,2,3]
print(aa == bb)
```

```javascript
aa = [1,2,3]
bb = [1,2,3]
console.log(aa == bb)
```

```csharp
var aa = new int[]{1,2,3};
var bb = new int[]{1,2,3};
Console.WriteLine(aa == bb);
```

```java
Integer[] aa = new Integer[]{1,2,3};
Integer[] bb = new Integer[]{1,2,3};
System.out.println(aa == bb);
```

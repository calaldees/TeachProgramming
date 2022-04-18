Number Handling
---------------

Static/Compiled seem to be different to Dynamic/Interpreted. Let's look.

Run all of these

java
```java
int a = Integer.MAX_VALUE;
System.out.println(a);
System.out.println(a+1);
```

csharp
```csharp
int a = Int32.MaxValue;
Console.WriteLine(a);
Console.WriteLine(a+1);
```
https://en.wikipedia.org/wiki/Nuclear_Gandhi

python
```python
import sys
a = sys.maxsize
print(a)
print(a+1)
```

javascript
```javascript
let a = Number.MAX_SAFE_INTEGER;
console.log(a);
console.log(a+1);
Number.MAX_SAFE_INTEGER+1 === Number.MAX_SAFE_INTEGER+2
```




Stubs
-----

### python

```python
def bubbleSort(data):
    print('bubbleSort')
    # CODE GOES HERE!
    return data

if __name__ == '__main__':
    data = ['b', 'd', 'c', 'a']
    data = bubbleSort(data)
    print(data)
```

`python3 FILENAME.py`

### c#

```csharp
using System;

class MainClass {

  public static void Main (string[] args) {new MainClass();}
  public MainClass() {
    string[] data = new string[]{"b", "d", "c", "a"};
    data = bubbleSort(data);
    Console.WriteLine(String.Join(",", data));
  }

  String[] bubbleSort(String[] data) {
    Console.WriteLine("bubbleSort");
    // CODE GOES HERE!
    return data;
  }

}
```

### java

```java
class Main {

  public static void main(String[] args) {new Main();}
  Main() {
    String[] data = new String[]{"b", "d", "c", "a"};
    data = bubbleSort(data);
    System.out.println(String.join(",", data));
  }

  String[] bubbleSort(String[] data) {
    System.out.println("bubbleSort");
    // CODE GOES HERE!
    return data;
  }

}
```

`javac Main.java && java Main`

### javascript

```javascript
function bubbleSort(data) {
    console.log('bubbleSort');
    // CODE GOES HERE!
    return data
}

let data = ['b', 'd', 'c', 'a'];
data = bubbleSort(data);
console.log(data);
```

`node FILENAME.js`

### vb

```vb
Module VisualBasic

    Sub Main()
        Dim data() as String = {"b", "d", "c", "a"}
        data = bubbleSort(data)
        Console.WriteLine(Join(data, ","))
    End Sub

    Function bubbleSort(data as String()) As String()
        Console.WriteLine("bubbleSort")
        ' CODE GOES HERE!
        bubbleSort = data
    End Function

End Module
```

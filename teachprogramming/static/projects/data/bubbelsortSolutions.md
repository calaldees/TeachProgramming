
Solutions
---------


```vb
Module VisualBasic

    Sub Main()
        Dim data() as String = {"b", "d", "c", "a"}
        data = bubbleSort(data)
        Console.WriteLine(Join(data, ","))
    End Sub

    Function bubbleSort(data as String()) As String()
        Console.WriteLine("bubbleSort")
        Dim has_changed as Boolean = True
        Do While has_changed
            Console.WriteLine(Join(data, ","))
            has_changed = False
            For i As Integer = 0 To data.Length - 2
                Dim a as String = data(i)
                Dim b as String = data(i+1)
                Console.WriteLine("comparing "+i.toString()+":"+a+" with "+(i+1).toString()+":"+b)
                If a > b Then
                    Console.WriteLine("swap")
                    data(i) = b
                    data(i+1) = a
                    has_changed = True
                End If
            Next
        Loop
        bubbleSort = data
    End Function

End Module
```


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
    //Console.WriteLine("bubbleSort");
    bool has_changed = true;
    while (has_changed) {
      //Console.WriteLine(String.Join(",", data));
      has_changed = false;
      for (int i=0 ; i<data.Length-1 ; i++) {
        string a = data[i];
        string b = data[i+1];
        //Console.WriteLine("comparing "+i+":"+a+" with "+(i+1)+":"+b);
        if (string.Compare(a,b) > 0) {
          //Console.WriteLine("swap");
          data[i] = b;
          data[i+1] = a;
          has_changed = true;
        }
      }
    }
    return data;
  }

}
```

```java
class Main {

  public static void main(String[] args) {new Main();}
  Main() {
    String[] data = new String[]{"b", "d", "c", "a"};
    data = bubbleSort(data);
    System.out.println(String.join(",", data));
  }

  String[] bubbleSort(String[] data) {
    //System.out.println("bubbleSort");
    Boolean has_changed = true;
    while (has_changed) {
      //System.out.println(String.join(",", data));
      has_changed = false;
      for (Integer i=0 ; i < data.length-1 ; i++) {
        String a = data[i];
        String b = data[i+1];
        //System.out.println("comparing "+i+":"+a+" with "+(i+1)+":"+b);
        if (a.compareTo(b) > 0) {
          //System.out.println("swap");
          data[i] = b;
          data[i+1] = a;
          has_changed = true;
        }
      }
    }
    return data;
  }

}
```




```python
def bubbleSort(data):
    """
    >>> bubbleSort(['a', 'b', 'c', 'd'])
    ['a', 'b', 'c', 'd']
    >>> bubbleSort(['b', 'd', 'c', 'a'])
    ['a', 'b', 'c', 'd']
    """
    #print('bubbleSort')
    has_changed = True
    while has_changed:
        #print(data)
        has_changed = False
        for i in range(len(data)-1):
            a = data[i]
            b = data[i+1]
            #print(f'comparing {i}:{a} with {i+1}:{b}')
            if a > b:
                #print(f'swap')
                data[i] = b
                data[i+1] = a
                has_changed = True
    return data

if __name__ == '__main__':
    data = ['b', 'd', 'c', 'a']
    data = bubbleSort(data)
    print(data)
```

```javascript
function bubbleSort(data) {
    //console.log('bubbleSort');
    let has_changed = true;
    while (has_changed) {
        //console.log(data);
        has_changed = false;
        for (i=0 ; i<data.length-1; i++) {
            let a = data[i];
            let b = data[i+1];
            //console.log(`comparing ${i}:${a} with ${i+1}:${b}`);
            if (a > b) {
                //console.log('swap');
                data[i] = b;
                data[i+1] = a;
                has_changed = true;
            }
        }
    }
    return data
}

let data = ['b', 'd', 'c', 'a'];
data = bubbleSort(data);
console.log(data);
```

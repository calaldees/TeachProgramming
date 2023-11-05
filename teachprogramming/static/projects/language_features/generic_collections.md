Generic Collections (implementation abstraction)
-------------------

java
```java
// Predict what this program should print (preferably discuss your idea with another person)
// then run it
// Can you describe why this has happened?
// Is this good? or bad?

// https://docs.oracle.com/javase/8/docs/technotes/guides/collections/overview.html
// https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html
import java.util.Arrays;
import java.util.Collection;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.TreeSet;

class Main {
  public static void main(String[] args) {
    System.out.println("Hello world!");

    Collection<Integer> a = new ArrayList<>();
    Collection<Integer> b = new LinkedList<>();
    Collection<Integer> c = new TreeSet<>();

    a.add(1);
    a.add(1);

    b.add(2);
    b.add(2);

    c.add(3);
    c.add(3);

    Collection<Integer> d = new ArrayList<>();
    d.addAll(a);
    d.addAll(b);
    d.addAll(c);

    System.out.println(
        String.join(",", Arrays.toString(d.toArray()))
    );
  }
}
```

* [Java Collections Framework](https://docs.oracle.com/javase/8/docs/technotes/guides/collections/overview.html)
    * Ability to abstract the implementation from the interface
    * [java.util.Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html)
        * List, Set, Map

Whiteboard/Visualiser?

* Arrays
    * Performant random access
    * Performant sequential access (cacheing)
    * Memory efficient
    * Difficult to add/remove/splice
        * Entire array needs copying to another location
* LinkedList
    * Sequential only access
        * not cacheable
    * Memory
        * Every element stores an additional next-reference
        * Can be distributed across memory 
    * Easy to add/remove/splice

* High level vs Low level
    * This example shows us first hand the difference between high level and low level languages.
    * In high level languages, we don't know what the system is doing. We use whatever abstraction we are provided.
    * in Low level languages we need to explicitly describe our implementation

* Microsoft C# [When to use generic collections](https://learn.microsoft.com/en-us/dotnet/standard/collections/when-to-use-generic-collections)
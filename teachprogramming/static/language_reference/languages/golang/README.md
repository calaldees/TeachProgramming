# TODO

https://devhints.io/go
https://gobyexample.com/
https://gophercises.com/


### [GoLang](https://golang.org/)

* Google's static typed, compiled performant systems level, concurrency primitives.
* Compiling C was too slow. They wanted something that compiles FAST.
* Modern language features
* Readability
* Very well designed standard library - fewer external libraries (including few gui)
* builtin formatter
* Not OO


> Java has explicit class: the Rectangle class declares it implements the interface `Shape`.
> Go’s approach is implicit. A structure that implements all functions of an interface - implicitly implements this interface.

* From [How WhatsApp scaled to 1 billion users with only 50 engineers](https://www.quastor.org/p/how-whatsapp-scaled-to-1-billion)
    * [Why you can have millions of Go-routines but only thousands of Java Threads](https://rcoh.me/posts/why-you-can-have-a-million-go-routines-but-only-1000-java-threads/)
        * If you’ve been working with JVM based languages for a while, you’ve probably come across a situation where you’ve reached the limit of the number of concurrent threads you can have.
        * On your personal computer, this limit is usually around ~10,000 threads.
        * On the other hand, you can have more than a hundred million goroutines on a laptop with Go.
        * This article explores why you can have so many more Goroutines than threads.
        * There’s two main reasons why
            * The JVM delegates threading to operating system threads. Go implements its own scheduler that allows many Goroutines to run on the same OS thread.
            * The JVM defaults to a 1 MB stack per thread. Go’s stacks are dynamically sized and a new goroutine will have a stack of about 4 KB.

FizzBuzz
========

* [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz#Programming_interviews) [_](https://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/)
    * > Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
    * In under 5min (Pro) - in under 10min (A Grade)
    * [Tom Scott commentary and solution](https://www.youtube.com/watch?v=QPZ0pIK_wsc) 7min

Hints
-----

* If you say "done it" to your interviewer and you have not fulfilled the criteria, you will look like a chump! Understand the problem before you start!
* Consider thinking of your test cases in advance and creating these before you start coding.

Python has built in `assert`
Here is a helper for csharp

```csharp
void AssertIsEqual<A> (A a, A b) {AssertIsEqual(a,b,"");}
void AssertIsEqual<A> (A a, A b, string message) {
    if (!a.Equals(b)) {
        throw new Exception($"Failed AssertIsEqual({a} == {b}): {message}");
    }
}
```

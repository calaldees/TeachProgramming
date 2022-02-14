In a Row
========

Create a function that returns the maximum number of the same item in a row.


```
    >>> in_a_row('')
    0
    >>> in_a_row('a')
    1
    >>> in_a_row('b')
    1
    >>> in_a_row('ab')
    1
    >>> in_a_row('aa')
    2
    >>> in_a_row('aab')
    2
    >>> in_a_row('abb')
    2
    >>> in_a_row('aabbcc')
    2
    >>> in_a_row('aabbbcc')
    3
    >>> in_a_row('aabbbccb')
    3
    >>> in_a_row('aabbbcacbaa')
    3
```

<details>
<summary>Hints: Approach</summary>

* Starting point: maybe create a function that counts the number of occurrences of an element in data
    * ```
        >>> count_item('a', "abcba")
        2
        ```
</details>


<details>
<summary>Professional</summary>

Professionals can make this generic, so that it can be used for multiple types of data
```
    >>> in_a_row((1,2,2,3,3,3,2,2))
    3
```
Can you also return the item that has been repeated that many times
```csharp
(int count, T i) in_a_row<T> (IEnumerable<T> data) {
    //???
}

AssertIsEqual(in_a_row("aabbbccb"), (3, 'b'), "should count 3 b's");
```
</details>
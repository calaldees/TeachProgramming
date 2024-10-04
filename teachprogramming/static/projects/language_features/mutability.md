Mutability
----------

javascript
```javascript
// Predict what this program should print (preferably discuss your idea with another person)
// then run it
// Can you describe why this has happened?
// Is this good? or bad?

function sum_numbers(numbers) {
    let total = 0;
    for (i of numbers) {
        total += i;
    }
    numbers.push(8);
    return total;
}

const ll = [1,2,3];
console.log(sum_numbers(ll));
console.log(sum_numbers(ll));
console.log(ll);
```

* Why is `const` not working?
* We can't inspect every method that could ever be run to verify it does not modify our data
* In `C`, `get` operation modify the dictionary to include the key. WARNING.
* Mutability by default is dangerous. It is difficult to protect yourself.
* Solution _Immutability_. Library's?
    * [immutable-js](https://immutable-js.com/)


Language Design Consistency
---------------------------

Lists are mutable.
Some list methods return new lists, some modify the list.


```javascript
aa = [4,3,1,2]
bb = aa.filter((i)=> i > 2)
console.log(aa)
console.log(bb)
// the original list is not altered
```

```javascript
aa = [4,3,1,2]
bb = aa.sort()
console.log(aa)
console.log(bb)
// the original list is altered
```

Problem: The language is not consistent. We have to study the language documentation to understand if a language has side effects
See ES2023 for array mutability

Further Reading
---------------

* Elixer: [Serialization is the Secret](https://www.zachdaniel.dev/p/serialization-is-the-secret)
  * Rebinding is not mutation
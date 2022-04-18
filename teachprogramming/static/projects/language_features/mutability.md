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

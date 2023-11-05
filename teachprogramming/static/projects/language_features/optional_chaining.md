Optional Chaining
=================

Javascript


* `?.` Operator
    * https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining
    *   ```javascript
        const adventurer = {
            name: 'Alice',
            cat: {
                name: 'Dinah',
            },
        };

        const dogName = adventurer.dog?.name;
        console.log(dogName);
        // Expected output: undefined

        console.log(adventurer.someNonExistentMethod?.());
        // Expected output: undefined
        ```
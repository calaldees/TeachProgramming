Async + await and the Event Loop
--------------------------------

* See [[concurrency]]
* Further reading
    * [henriqueinonhe/promises-training](https://github.com/henriqueinonhe/promises-training/)
        * > Practice working with promises through a curated collection of interactive challenges. This repository provides a platform to refine your skills, complete with automated tests to to give you instant feedback and validate your progress. 

javascript
```javascript
// Part 1: ---
// Predict what this program should print (preferably discuss your idea with another person)
// then run it
// Can you describe why this has happened?
// Is this good? or bad?
console.log("1");
const _ = setTimeout(()=>{
    console.log("2");
}, 1000);
console.log("3");

// Part 2: ---
// Alter the program above to ensure the program
// prints `1`
// _waits for 1 second_
// prints `2`
// _waits for 1 second_
// prints `3`
```

```javascript
// Run this code
// try and work out what the hell is going on ...
const promise = new Promise((resolve, reject) => {
    // do a chunk of work here
    // this work will be done in the background
    // (that's not the whole story, but close enough)
    // when we are finished this chunk call `resolve()`
    resolve("some work has been done");
    // or call reject() if it's broken
}).then((data)=>{
    // another chunk of work in the background
    return data + " and even more work";
}).then((data)=>{
    console.log(data);
}).catch((error)=>{
    console.error(error);
});
// we can query the `promise` object to check if our background work has finished
```

Javascript in single threaded. Without breaking work in to chunks it would lock the whole system.

```javascript
function sleep(milliseconds) {
    return new Promise((resolve, reject) => setTimeout(()=>resolve(Date.now()), milliseconds));
}
async function do_steps() {
    console.log("1");
    const _a = await sleep(1000);
    console.log("2", _a);
    const _b = await sleep(1000);
    console.log("3", _b);
    const _c = await sleep(1000);
    console.log("4", _c);
}
const promise = do_steps();
// Now imagine if `sleep(1000)` was replaced with `fetch("http://my.service.com/api/v1/do_stuff?name=me")`
```

* Python and Javascript are "single process" technologies. They simply cannot support concurrency (without spawning more process's)
* [What Is the Python Global Interpreter Lock (GIL)?](https://realpython.com/python-gil/)
* We can augment these single process languages to be utilising that single process as much as possible by using an event loop. This helps with blocking IO.
    * The languages have new features `async` and `await` to support this



Misunderstanding example - Cypress
----------------------------------
https://docs.cypress.io/faq/questions/using-cypress-faq#How-do-I-get-an-element-s-text-contents

```javascript
// INCORRECT USEAGE!! Cypress is async all the way
console.log(1)
let text = cy.contains(uuid).should('be.visible').parents('li').find('[data-field="id"]').invoke('text')
console.log(2)
if (text == "thing") {
    console.log(3.5)
}
console.log(3)
cy.get('textarea').type(text)
// All the console.log happen instantly
```

Further reading
---------------

* [How to Use Fetch with async/await](https://dmitripavlutin.com/javascript-fetch-async-await/)
    * Concurrent fetches


---


```python
t.Callable[[URLParams], t.Awaitable[APIPayload]]
```
Explanation of t.Awaitable pattern https://stackoverflow.com/a/59177557/3356840

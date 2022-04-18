Prototypical Inheritance
------------------------

javascript
```javascript
// from https://blog.frankel.ch/six-interesting-features-programming-languages/

// Part 1: ----
class Person {
  constructor(name, birthdate) {
    this.name = name;
    this.birthdate = birthdate;
  }
}
const person1 = new Person("John Doe", Date.now());
const person2 = new Person("Jane Doe", Date.now());

// Try (before running each line, predict what it will do)
// person1.name
// person2.name
// person1.debug()

// Part 2: ----
person1.debug = function() {
  console.debug("I added this dynamically to a single object", this);
}
person1.debug();

// Try (before running each line, predict what it will do)
// person1.debug()
// person2.debug()

// Part 3: ----
Person.prototype.debug = function() {
  console.debug("I added this to everyone", this);
}
const person3 = new Person("Nicolas", Date.now());

// Try (before running each line, predict what it will do)
// person1.debug();
// person2.debug();
// person3.debug();


// Part 4: ---
// Question: What has just happened?
// What is _prototypical inheritance_?
// Is this good? or bad?
```

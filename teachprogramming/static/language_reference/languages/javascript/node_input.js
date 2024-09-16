/*
const rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
});


await rl.question('What is your age? ', (age) => {console.log('Your age is: ' + age);});

//await rl.question("hi",(a)=>{console.log(a)})

const readlinePromises = require('node:readline/promises');
const rl = readlinePromises.createInterface({
  input: process.stdin,
  output: process.stdout,
}); 
const answer = await rl.question('What is your favorite food? ');
console.log(`Oh, so your favorite food is ${answer}`);


*/


// MY GOD this took far to long ...

// docker run --rm -it --volume ${PWD}:/temp/:ro node /temp/node_input.js

//const fileStream = fs.createReadStream('input.txt');
const rl = require('readline').createInterface({
  input: process.stdin, //or fileStream 
  output: process.stdout,
  terminal: false,
})
async function input() {for await (const line of rl) {return line}}
(async () =>{
    //for await (const line of rl) {console.log("Echo> " + line)}
    console.log("Say somethiong: ")
    const answer = await input()
    console.log(`You answered ${answer}`)
})()

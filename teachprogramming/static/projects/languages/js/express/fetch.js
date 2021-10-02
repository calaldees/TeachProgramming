import fetch from 'node-fetch';

const postcode = "CT1 1QR";

/*
fetch(`https://api.postcodes.io/postcodes/${postcode}`)
    .then(response => response.json())
    .then(data=>{
        console.log(data);
    })
.catch(err => console.error(err));
*/

// https://www.geeksforgeeks.org/difference-between-promise-and-async-await-in-node-js/?ref=leftbar-rightbar

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}



console.log(1);

const string1 = "geeksforgeeks";
const string2 = "geeksforgeeks";

const promise = new Promise(function (resolve, reject) {

    console.log(2);

    if (string1 === string2) {
        const ss = string1 + string2;
        resolve(ss);
    } else {
        reject("nothing");
    }

    console.log(3);
});

console.log(4);

promise
    .then(d => {
        console.log(5);
        return d + " some more stuff";
    })
    .then(d => {
        console.log(6);
        console.log("Promise resolved successfully", d);
    })
    .catch(d => {
        console.log(7);
        console.log("Promise is rejected", d);
    });

console.log(8);


async function evaluate_promise() {
    console.log(9);
    const output = await promise;
    console.log("finished async", output);
    await sleep(100);
    console.log(10);
}
console.log(11);
evaluate_promise();
console.log(12);
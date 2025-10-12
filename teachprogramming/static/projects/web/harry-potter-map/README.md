
https://www.deviantart.com/littlefallingstar/art/The-Marauders-Map-389921556

* https://harrypotter.fandom.com/wiki/Marauder%27s_Map
* YouTube [The Marauder's Map | Harry Potter and the Prisoner of Azkaban](https://youtu.be/ZSf_o02Yv60?si=F9vLcVEG_Ny404ut&t=44)

Use Web Geoposition
Server to colate positions
websocket event for positions

interpolate foosteps on client


Try to avoid dependencies - from scratch

https://www.emqx.com/en/blog/connect-to-mqtt-broker-with-websocket


Chat GPT 3.5
============

Question
--------

I have a geometric maths problem that I want to solve with javascript or python.

I have two sets of four co-ordinates that represent a 2D space. e.g:

Space 1 is defined by
X1,y1 x2,y2 x3,y3 x4,y4
(-1,1) (-3,-1) (3,-2) (1,2)

Space 2 is defined by
x5,y5 x6,y6 x7,y7 x8,y8
(2,2) (2,0) (4,0) (4,2)

I want a function that given (x9,y9) from co-ordinate space1 would return the equivalent (x10,y10) in coordinate space2 
e.g:
(-1,1) -> (2,2)
(0.1,-0.5)? -> (3,1)? my guess approximate
(2.5,-1.5)? -> (3.7,0.3)? my guess approximate

What code would I write to solve this problem?


Answer
------

To solve this problem, you can use affine transformations, specifically, the transformation matrix that maps points from one coordinate space to another. In 2D, this transformation matrix can be represented as a 3x3 matrix.

Here's a JavaScript function that takes coordinates from space1 and returns the equivalent coordinates in space2 using an affine transformation:

```javascript
function transformCoordinates(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9) {
    // Create matrices for space1 and space2
    const matrixSpace1 = math.matrix([[x1, x2, x3, x4], [y1, y2, y3, y4], [1, 1, 1, 1]]);
    const matrixSpace2 = math.matrix([[x5, x6, x7, x8], [y5, y6, y7, y8], [1, 1, 1, 1]]);

    // Calculate the transformation matrix
    const transformMatrix = math.multiply(matrixSpace2, math.inv(matrixSpace1));

    // Create a vector for the input coordinates
    const inputVector = math.matrix([[x9], [y9], [1]]);

    // Apply the transformation
    const outputVector = math.multiply(transformMatrix, inputVector);

    // Extract the transformed coordinates
    const x10 = outputVector.get([0, 0]);
    const y10 = outputVector.get([1, 0]);

    return { x10, y10 };
}

// Example usage
const result = transformCoordinates(-1, 1, -3, -1, 3, -2, 1, 2, 2, 2, 2, 0, 4, 0, 4, 2, -0.1, -0.5);
console.log(result); // Output: { x10: 3.2611940298507465, y10: 0.25373134328358384 }
```

This example uses the `math` library for matrix operations. You can install it using:

```bash
npm install mathjs
```

Please note that the transformation matrix is calculated by finding the inverse of the matrix representing space1 and then multiplying it with the matrix representing space2. The resulting matrix can be used to transform coordinates from space1 to space2. The function then returns the transformed coordinates as an object.


Code
====

https://cdnjs.com/libraries/mathjs

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/12.2.1/math.min.js" integrity="sha512-hNhZseI4UffZ3L9lqew2Jqi11l/m7ZSf1snwdIjC9vqi4DCzMf4pip+rlMMD+5LQbzCA15ebOEOGLnMu0vd+eg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
```

```javascript
//import mathjs from 'https://cdn.jsdelivr.net/npm/mathjs@12.2.1/+esm'  // https://www.jsdelivr.com/package/npm/mathjs
import * as mathjs from 'https://esm.run/mathjs'

let [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8] = [-1, 1, -3, -1, 3, -2, 1, 2, 2, 2, 2, 0, 4, 0, 4, 2]

const matrixSpace1 = mathjs.matrix([
    [x1, x2, x3, x4],
    [y1, y2, y3, y4],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
])
const matrixSpace2 = mathjs.matrix([
    [x5, x6, x7, x8],
    [y5, y6, y7, y8],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
])
const transformMatrix = mathjs.multiply(matrixSpace2, mathjs.inv(matrixSpace1))

function transformCoordinates(x,y) {
    const inputVector = mathjs.matrix([[x], [y], [1]])
    const outputVector = mathjs.multiply(transformMatrix, inputVector)
    return [outputVector.get([0, 0]), outputVector.get([1, 0])]
}

let [x, y] = transformCoordinates(-0.1, -0.5)

console.log(x,y)  // Output: 3.2611940298507465 0.25373134328358384
```


GPT4
----

I have a geometric maths problem that I want to solve with javascript in a web browser.

I have two sets of four coordinates (polygon) that represent a 2D space. e.g:

The 2d polygon for space1 is defined by the points
x1,y1 x2,y2 x3,y3 x4,y4
(-1,1) (-3,-1) (3,-2) (1,2)

The 2d polygon for space2 is defined by the points
x5,y5 x6,y6 x7,y7 x8,y8
(2,2) (2,0) (4,0) (4,2)

I want a function that given (x,y) from coordinate space1 would return the equivalent (x,y) in coordinate space2
e.g:
(-1,1) -> (2,2) as this is the corner point
(0.1,-0.5)? -> (3,1)? my guess approximate (this is the center of space2)
(2.5,-1.5)? -> (3.7,0.3)? my guess approximate (this is near the bottom right of space 2)

My assumption is that we need to derive a 3x3 affine transform matrix to transform from coordinate space1 to coordinate space2.

I assume I will need a javascript library to assist?
As a possibility; I can see that `mathjs` can be used in a browser as follows
```html
<script type="module">
import * as mathjs from 'https://esm.run/mathjs'

//mathjs.matrix
//mathjs.inv
//mathjs.multiply
//mathjs.transpose
</script>
```

What code would I write to solve this problem?
I'm assuming an interface something like
```javascript
function create_affine_transform_matrix(s1, s2) {
    return  // 3x3 affine transform matrix
}

const space1 = [[-1,1],[-3,-1],[3,-2],[1,2]]
const space2 = [[ 2,2],[ 2, 0],[4, 0],[4,2]]
const transform_matrix = create_affine_transform_matrix(space1, space2)

function transform_coord_space(transform_matrix, point1) {
    // return point2
}

let point2 = transform_coord_space(space1, space2, [0.1,-0.5])
// where `point2` is expected to be approximately [2,2]
```

GPT5
----

Win
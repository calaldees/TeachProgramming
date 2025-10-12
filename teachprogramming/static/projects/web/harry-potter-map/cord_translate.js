// https://mathjs.org/

//import mathjs from 'https://cdn.jsdelivr.net/npm/mathjs@15.0.0/+esm'
import mathjs from './math.js'  // curl --location-trusted https://cdnjs.cloudflare.com/ajax/libs/mathjs/14.8.1/math.min.js -o math.js

// https://wordsandbuttons.online/interactive_guide_to_homogeneous_coordinates.html

function create_projective_transform_matrix(src, dst) {
    // src and dst are arrays of 4 points: [[x,y], [x,y], [x,y], [x,y]]
    const A = []
    const b = []
    for (let i = 0; i < 4; i++) {
        const [x, y] = src[i]
        const [X, Y] = dst[i]
        A.push([ x, y, 1, 0, 0, 0, -X*x, -X*y ])
        A.push([ 0, 0, 0, x, y, 1, -Y*x, -Y*y ])
        b.push(X)
        b.push(Y)
    }
    // Solve A * h = b
    return mathjs.lusolve(mathjs.matrix(A), mathjs.matrix(b)).valueOf().flat()
}

function transform_point(H, pt) {
    const [x, y] = pt
    const w = H[6]*x + H[7]*y + 1
    const X = (H[0]*x + H[1]*y + H[2]) / w
    const Y = (H[3]*x + H[4]*y + H[5]) / w
    return [X, Y]
}

// Export ----------------------------------------------------------------------

export function build_transform_point_function(space1, space2) {
    const H = create_projective_transform_matrix(space1, space2)
    console.debug("Transform matrix:", H)
    return (pt) => transform_point(H, pt)
}


// Tests -----------------------------------------------------------------------

export function assertEquals(comparison_tuples) {
    for (let [a, b] of comparison_tuples) {
        if (! (a==b)) {throw `${a} should-equal ${b}`}
        console.assert(a == b, `${a} should-equal ${b}`)
        // `console.assert` does nothing! It prints nothing .. I don't know why. A: Assertions are not enabled by default?
    }
}
export function assertEqualsObject(comparison_tuples) {
    return assertEquals(comparison_tuples.map(v => v.map(JSON.stringify)))
}

//const H = create_projective_transform_matrix(
//    [[-1,1],[-3,-1],[3,-2],[1,2]],
//    [[ 2,2],[ 2, 0],[4, 0],[4,2]],
//)
//console.log("Transform matrix:", H)
//console.assert(transform_point(H, [-1,1]), [2,2])
//console.assert(transform_point(H, [0.1,-0.5]), ??)
//console.assert(transform_point(H, [2.5,-1.5]), ??)


const test1 = build_transform_point_function(
    [[  0,  0],[100,  0],[100,100],[  0,100]],
    [[  0,  0],[200,  0],[200,200],[  0,200]],
)
assertEqualsObject([test1([  0,  0]),[  0,  0]])
assertEqualsObject([test1([100,100]),[200,200]])
assertEqualsObject([test1([ 50, 50]),[100,100]])

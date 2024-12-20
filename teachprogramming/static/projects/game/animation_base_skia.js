// Consider https://skia-canvas.org/ for local js rendering in node

import {Canvas} from 'skia-canvas'

let canvas = new Canvas(400, 400)
let ctx = canvas.getContext("2d")
let {width, height} = canvas

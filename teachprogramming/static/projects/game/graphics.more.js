// Solution Shape ----------------------------------------------------------

function sides(c, x, y, sides, size) {
    const storedTransform = c.getTransform()
    c.translate(x,y)
    c.beginPath()
    for (let i=0 ; i<=sides ; i++) {
        c.lineTo(0, Math.floor(size)+0.5)
        c.translate(0,size)
        c.rotate((Math.PI*2)/sides)
    }
    c.stroke()
    c.fill()
    c.setTransform(storedTransform)
}
let state = {frame: 0, x: 50, y:50, angle:0}
function updateState(s) {
    s.frame += 1
    s.x += Math.sin(s.frame/10)*5
    s.angle += 0.01
}
function render2(c, s) {
    reset()
    c.translate(s.x,s.y)
    c.rotate(s.angle)
    sides(context, 0, 0, 6, 20)
}
function startAnimation(time) {
    requestAnimationFrame(startAnimation)
    updateState(state)
    render2(context, state)
}
startAnimation()

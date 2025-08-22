function createFullScreenCanvasElement({width=640, height=360, background_color='black'}={}) {
    const body_style = `
        margin: 0;
        height: 100%;
        overflow: hidden;
        text-align: center;
        background-color: ${background_color};
    `
    document.body.style = body_style
    document.documentElement .style = body_style

    const _canvas_attrs = {
        width: width,
        height: height,
        style: `
            image-rendering: pixelated;
            object-fit: cover;
            height: 100%; max-height: 100%;
            max-width: 100%;
        `,
    }
    const canvas = document.createElement('canvas')
    for (let [k, v] of Object.entries(_canvas_attrs)) {canvas.setAttribute(k,String(v))}
    document.body.appendChild(canvas)

    return canvas
}

function createAudioElement() {
    let audio = document.getElementById('audio')
    if (!audio) {
        audio = new Audio()
        document.body.appendChild(audio)
    }
    audio.addEventListener("loadeddata", (e) => audio.play())
    return audio
    // https://developer.mozilla.org/en-US/docs/Web/API/HTMLAudioElement
    //play_audio = (url) => {this.audio.src = url}
}

export class CanvasAnimationBase {
    constructor(canvas=undefined, fps=60, canvas_attrs={background_color: 'black'}) {
        this.canvas = canvas || createFullScreenCanvasElement(canvas_attrs)
        this.context = this.canvas.getContext('2d', { alpha: true })
        // TODO: getContext('2d', { alpha: false }) https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas#turn_off_transparency

        this.audio = createAudioElement()
        this.play_audio = (url) => {this.audio.src = url}

        this.images = {}

        window.addEventListener("focus", () => {this.setRunning(true)} , false)
	    window.addEventListener("blur" , () => {this.setRunning(false)}, false)

        this.keys_pressed = new Set()
        window.addEventListener('keydown', (e) => this.keys_pressed.add(e.key), true)
        window.addEventListener('keyup'  , (e) => this.keys_pressed.delete(e.key), true)
        this.mouse_x = 0
        this.mouse_y = 0
        this.canvas.addEventListener('mousemove', (e) => {
            const r = e.target.getBoundingClientRect()
            this.mouse_x = Math.floor((e.clientX - r.left) / (this.canvas.clientWidth/this.canvas.width))
            this.mouse_y = Math.floor((e.clientY - r.top ) / (this.canvas.clientHeight/this.canvas.height))
        }, true)

        this.frame = 0
        this.milliseconds_per_frame = 1000/fps

        //this.setRunning(true)  // race hazzard in starting?
    }

    get w() {return this.canvas.width}
    get h() {return this.canvas.height}
    get canvas_aspect_ratio() {return this.w / this.h}
    get window_aspect_ratio() {return window.innerWidth / window.innerHeight}

    clear = () => {
        this.context.clearRect(0, 0, this.w, this.h)
        //c.fillStyle = COLOR.black
        //c.fillRect(0, 0, w, h)
    }

    setRunning = (running) => {
        console.log("setRunning", running)
        this.running = running
        if (!this.running && this.requestAnimationFrameId) {
            cancelAnimationFrame(this.requestAnimationFrameId)
            this.requestAnimationFrameId = undefined;
        } else if (running && !this.requestAnimationFrameId) {
            this.run()
        }
    }

    load_image = (name, url) => {
        let resolve_image_loaded = undefined
        const promise = new Promise((resolve, reject) => {
            resolve_image_loaded = resolve
        })
        const images = this.images
        images[name] = new Image()
        images[name].onload = function() {
            images[name] = this
            resolve_image_loaded(this)
        }
        images[name].src = url
        return promise
    }

    run = (time) => {
        if (this.keys_pressed.has("Escape")) {this.setRunning(false)}
        if (!time) {this.epoch = undefined}
        if (!this.epoch && time) {this.epoch = time - (this.frame * this.milliseconds_per_frame)}
        const frame = Math.floor((time - this.epoch) / this.milliseconds_per_frame)
        const draw_required = this.frame<frame;
        for ( ; this.frame<frame ; this.frame++) {this.model_inc(this.frame)}
        if (draw_required) {this.draw(this.context, this.frame)}
        // TODO: Is it worth drawing to a backbuffer and drawing this backbuffer IMMEDIATELY on `.run`?
        if (this.running) {this.requestAnimationFrameId = requestAnimationFrame(this.run)}
    }

    model_inc(frame) {
        throw new Error("Not Implemented Error")
    }
    draw(context, frame) {
        throw new Error("Not Implemented Error")
    }

    // Graphics Utils ----------------------------------------------------------

    static drawLine(c, x1,y1,x2,y2,color='white',lineWidth=1) {
        c.strokeStyle = color
        c.lineWidth = lineWidth
        c.beginPath()
        c.moveTo(x1, y1)
        c.lineTo(x2, y2)
        c.stroke()
    }

    static subsurface(img, x, y, width, height) {
        const o = new OffscreenCanvas(width, height)
        const c = o.getContext("2d")
        c.drawImage(img, -x, -y)
        return o.transferToImageBitmap()
    }

    static invert(img) {
        const o1 = new OffscreenCanvas(img.width, img.height)
        const c1 = o1.getContext("2d")
        // Invert image (but destroys transparency)
        c1.drawImage(img, 0, 0)
        c1.globalCompositeOperation='difference'
        c1.fillStyle='white'
        c1.fillRect(0, 0, img.width, img.height)

        // Mask
        const o2 = new OffscreenCanvas(img.width, img.height)
        const c2 = o2.getContext('2d')
        c2.drawImage(img, 0, 0);
        c2.globalCompositeOperation = 'source-in';
        c2.fillStyle = 'black';
        c2.fillRect(0, 0, img.width, img.height);

        // Cut Mask out of Inverted image
        c1.globalCompositeOperation = 'destination-in';
        c1.drawImage(o2, 0, 0);
        return o1.transferToImageBitmap()
    }

}

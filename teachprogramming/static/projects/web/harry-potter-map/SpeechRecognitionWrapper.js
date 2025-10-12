const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition

export class SpeechRecognitionWrapper {
    constructor(phrases=[], element_root=document.body) {
        if (!SpeechRecognition) {
            console.error("SpeechRecognition unsupported")
            return
        }
        this.recognition = undefined

        console.log("SpeechRecognition supported - hold key/mouse to listen")
        element_root.addEventListener('keydown', this._start)
        element_root.addEventListener('mousedown', this._start)
        element_root.addEventListener('mouseup', this._stop)
        element_root.addEventListener('keyup', this._stop)

        this.registerPhrases(phrases)
    }

    registerPhrases(phrases) {
        // TODO: parse phrases - we need to assert the structure is correct
        this.phrases = [...this.phrases, ...phrases]
    }

    onSpeechResult(speech_event) {
        const transcript = speach_event.results[0][0].transcript
        console.log('recognition', transcript, `Confidence: ${speech_event.results[0][0].confidence}`)
        const transcript_split = transcript.toLowerCase().split(' ')
        for (let {keywords, func} of this.phrases) {
            if (all(keywords.map((k)=>transcript_split.includes(k.toLowerCase())))) {
                func()  // trigger the function as all keywords are in the transcript
                return
            }
        }
    }

    _start() {
        if (this.recognition) {return}
        recognition = new SpeechRecognition()
        recognition.continuous = false
        recognition.lang = "en-UK"
        recognition.interimResults = false
        recognition.onresult = onSpeechResult
        recognition.onspeechstart = () => {console.log('onspeechstart')}
        recognition.onspeechend = this._stop
        console.log("recognition.start()")
        recognition.start()
    }

    _stop() {
        if (!this.recognition) {return}
        console.log("recognition.stop()")
        recognition.stop()
        this.recognition = undefined
    }
}
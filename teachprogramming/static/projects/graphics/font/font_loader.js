import { range, zip, fetch_text } from './core.js'
import { Gfx } from './animation_base.js'

// From Img --------------------------------------------------------------------

export const SEQUENCE_DAMIENG = ` !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_£abcdefghijklmnopqrstuvwxyz{|}~©`.replace('\n','')

export function cut_font_chars_from_img(img, char_seq, w=8, h=8) {
    const [ww, hh] = [img.width, img.height]
    return Object.fromEntries(
        [...range(Math.min(Math.floor(ww/w)*Math.floor(hh/h),char_seq.length))].map((i)=>[
            char_seq[i], Gfx.subsurface(img, (i*w)%ww, Math.floor((i*w)/ww)*h, w, h)
        ])
    )
}

// From text `yaff`  -----------------------------------------------------------

function text_char_to_ImageData(char, foreground='@', width=8, height=8) {
    const [WHITE_PIXEL, BLACK_PIXEL] = [[255,255,255,255],[0,0,0,0]]
    const pixel_data = [...char].map(c=>c==foreground?WHITE_PIXEL:BLACK_PIXEL).flat()
    return new ImageData(new Uint8ClampedArray(pixel_data), width, height)
}
function* _parse_yaff(text, foreground='@', background='.', width=8, height=8) {
    const REGEX_UNICODE_LABEL_AND_CHAR = new RegExp(String.raw`u\+([0123456789abcdef]+):(.+?)\n\n`, "igs")
    const REGEX_CHAR = new RegExp(String.raw`[${background}${foreground}]{${width*height}}`, "isg")
    for (let match of text.matchAll(REGEX_UNICODE_LABEL_AND_CHAR)) {
        let [_, unicode, text_char] = match
        if (text_char=text_char.replaceAll(/\s/sg, '').match(REGEX_CHAR)[0]) {
            yield [
                String.fromCharCode(parseInt('0x'+unicode,16)),
                text_char_to_ImageData(text_char,foreground,width,height),
            ]
        }
    }
}
export async function parse_yaff(filename) {
    const oo = Object.fromEntries(_parse_yaff(await fetch_text(filename)))
    return Object.fromEntries(zip(
        Object.keys(oo),
        await Promise.all(Object.values(oo).map(i=>createImageBitmap(i))),
    ))
}

// From text `draw`  -----------------------------------------------------------

function* extract_font_text_chars(text, foreground='@', background='.', width=8, height=8) {
    const REGEX_CHAR = new RegExp(String.raw`[${background}${foreground}]{${width*height}}`, "isg")
    for (let match of text.replaceAll(/\s/sg, '').matchAll(REGEX_CHAR)) {yield match[0]}
}
export async function parse_draw(filename, char_seq) {
    const text = await fetch_text(filename)
    return Object.fromEntries(zip(
        char_seq,
        await Promise.all(
            [...extract_font_text_chars(text)]
            .map(c=>text_char_to_ImageData(c,'#',8,8))
            .map(i=>createImageBitmap(i)),
        )
    ))
}

export const SEQUENCE_AMSTRAD = String.raw`◻⎾⏊⏌⚡︎⊠✓⍾←→↓↑↡↲⊗⊙⊟◷◶◵◴⍻⎍⊣⧖⍿␦⊖◰◱◲◳!"#$%&’()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]↑_\`abcdefghijklmnopqrstuvwxyz{|}~  ▘▝▀▖▌▞▛▗▚▐▜▄▙▟█·╵╶└╷│┌├╴┘─┴┐┤┬┼^´¨£©¶§‘¼½¾±÷¬¿¡αβγδεθλμπσφψχωΣΩ🮠🮡🮣🮢🮧🮥🮦🮤🮨🮩🮮╳╱╲🮕▒▔▕▁▏◤◥◢◣🮎🮍🮏🮌🮜🮝🮞🮟☺☹♣♦♥♠○●□■♂♀♩♪☼🙭⭣⭠⭢▲▼▶◀🯆🯅𜱣🯈⭥⭤`

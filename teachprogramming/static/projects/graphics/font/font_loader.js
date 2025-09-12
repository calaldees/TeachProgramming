import { range, zip, fetch_text } from './core.js'
import { Gfx } from './animation_base.js'


function* remove_dupe_chars(arr) {
    const seen = new Set()
    for (let i of arr) {
        // Skip variation selector VS15
        // https://en.wikipedia.org/wiki/Variation_Selectors_(Unicode_block)
        // https://www.codetable.net/decimal/65038
        if (i.charCodeAt()==65038) {continue}
        if (seen.has(i)) {yield undefined}
        else {seen.add(i); yield i}
    }
}

// From Img --------------------------------------------------------------------

export const SEQUENCE_DAMIENG = `
 !"#$%&'()*+,-./0123456789:;<=>?
@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_
£abcdefghijklmnopqrstuvwxyz{|}~©
`.replaceAll('\n','')

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
    const [foreground, background, width, height] = ['#', '-', 8, 8]
    const text = await fetch_text(filename)
    return Object.fromEntries(zip(
        remove_dupe_chars(char_seq),
        await Promise.all(
            [...extract_font_text_chars(text,foreground,background)]
            .map(c=>text_char_to_ImageData(c,foreground,width,height))
            .map(i=>createImageBitmap(i)),
        )
    ))
}

// https://en.wikipedia.org/wiki/Amstrad_CPC_character_set
export const SEQUENCE_AMSTRAD = `
◻⎾⏊⏌⚡︎⊠✓⍾←→↓↑↡↲⊗⊙
⊟◷◶◵◴⍻⎍⊣⧖⍿␦⊖◰◱◲◳
 !"#$%&’()*+,-./
0123456789:;<=>?
@ABCDEFGHIJKLMNO
PQRSTUVWXYZ[\\]↑_
\`abcdefghijklmno
pqrstuvwxyz{|}~⌫
 ▘▝▀▖▌▞▛▗▚▐▜▄▙▟█
 ·╵╶└╷│┌├╴┘─┴┐┤┬┼
^´¨£©¶§‘¼½¾±÷¬¿¡
αβγδεθλμπσφψχωΣΩ
🮠🮡🮣🮢🮧🮥🮦🮤🮨🮩🮮╳╱╲🮕▒
▔▕▁▏◤◥◢◣🮎🮍🮏🮌🮜🮝🮞🮟
☺☹♣♦♥♠○●□■♂♀♩♪☼🚀
🙭⭣⭠⭢▲▼▶◀🯆🯅𜱣🯈⭥⭤
`.replaceAll('\n','')

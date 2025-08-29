import { range, zip } from './core.js'
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

// From text (yaff,draw) -------------------------------------------------------

function* extract_font_text_chars(text, foreground='@', background='.', width=8, height=8) {
    text = text.replaceAll(/\s/sg, '')
    const REGEX_CHAR = new RegExp(String.raw`[${background}${foreground}]{${width*height}}`, "isg")
    for (let match of text.matchAll(REGEX_CHAR)) {yield match[0]}
}
function* extract_unicode_sequence(text) {
    const REGEX_UNICODE = new RegExp(String.raw`u\+([0123456789abcdef]+):`, "ig")
    for (let match of text.matchAll(REGEX_UNICODE)) {
        yield String.fromCharCode(parseInt('0x'+match[1],16))
    }
}
function text_char_to_ImageData(char, foreground='@', width=8, height=8) {
    const [WHITE_PIXEL, BLACK_PIXEL] = [[255,255,255,255],[0,0,0,0]]
    const pixel_data = [...char].map(c=>c==foreground?WHITE_PIXEL:BLACK_PIXEL).flat()
    return new ImageData(new Uint8ClampedArray(pixel_data), width, height)
}
export async function parse_font_unicode(data, char_seq=undefined) {
    return Object.fromEntries(zip(
        char_seq || extract_unicode_sequence(data),
        await Promise.all(
            [...extract_font_text_chars(data)]
            .map(char=>text_char_to_ImageData(char))
            .map(async (img_data)=>await createImageBitmap(img_data)),
        )
    ))
}

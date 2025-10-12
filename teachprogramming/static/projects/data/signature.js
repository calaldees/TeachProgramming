const SEPARATOR = '::'
const SECRET = 'abc'
function _funcHash(data) {return createHash('sha256').update(data).digest('hex')}
function _funcTimestamp() {return Math.floor(new Date().getTime()/1000)}


function sign_message(data, secret=SECRET) {
    const timestamp = _funcTimestamp()
    const hash = _funcHash([data, timestamp, secret].join(''))
    return [data, timestamp, hash].join(SEPARATOR)
}

function verify_signed_message(msg, secret=SECRET) {
    const [data, timestamp, hash] = msg.split(SEPARATOR)
    const hash_expected = _funcHash([data, timestamp, secret].join())
    if (hash != hash_expected) {throw new Exception('signature failed')}
    return data
}


let msg = sign_message('MahMsg')
verify_signed_message(msg)

msg = msg.replace('MahMsg', 'TamperedMessage')
verify_signed_message(msg)

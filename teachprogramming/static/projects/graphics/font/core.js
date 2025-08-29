function* range(target, start=0, step=1) {for (let i=start ; i<target ; i+=step) {yield i}}
function* enumerate(iterable) {let count = 0; for (let item of iterable) {yield [count++, item]}}
function all(iterable) {for (let i of iterable) {if (!i) {return false}} return true}
function* zip(...iterables) {
    const iterators = [...iterables].map(iterable => iterable[Symbol.iterator]());
    while (true) {
        const iterable_items = iterators.map(iterator => iterator.next());
        if (all(iterable_items.map(i => i.done))) {break;}
        yield iterable_items.map(i => i.value);
    }
}
function clear_object(o) {Object.keys(o).forEach(k => {delete o[k]})}
async function fetch_text(path) {return await (await fetch(path)).text()}

export {
    range,
    enumerate,
    all,
    zip,
    clear_object,
    fetch_text,
}
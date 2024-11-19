
```javascript
function pad_line_number(lineNum, length=3) {
    return [...range(length)].reverse().map(i=>{
        const s = lineNum/Math.pow(10,i)
        return s<1?" ":Math.floor(s)%10
    }).join("")
}
assertEquals([
    [pad_line_number(123),"123"],
    [pad_line_number(987),"987"],
    [pad_line_number(55) ," 55"],
    [pad_line_number(10) ," 10"],
    [pad_line_number(3)  ,"  3"],
])
```
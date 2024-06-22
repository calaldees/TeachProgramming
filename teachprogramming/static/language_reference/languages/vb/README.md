```bash
function csharp { mcs "$1" && clear && mono "${1%.*}.exe" && rm "${1%.*}.exe"; }
function vb { vbnc "$1" && clear && mono "${1%.*}.exe" && rm "${1%.*}.exe"; }
```

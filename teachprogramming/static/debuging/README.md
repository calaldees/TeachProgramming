How to Debug

debug by `print`
breakpoint
    inspect state
    step
    step into
    stack
    continue - next breakpoint (multiple)
postmortem debugger

Principles - tools - language agnostic

Language examples



https://github.com/hchasestevens/tracing
```python
from tracing import tracing
with tracing():
  ...  # each line executed will be printed to stdout
```
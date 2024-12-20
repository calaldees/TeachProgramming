
try catch

> After forgetting what else does in try/else and for/else numerous times, I have mentally aliased it with noexcept and nobreak in those respective contexts.

```python
try:
  cs = x.cleanupSet
except AttributeError:
  pass
else:
  for v in cs:
    v.cleanup()
```


Other forms of error handling
Golang always returns an error
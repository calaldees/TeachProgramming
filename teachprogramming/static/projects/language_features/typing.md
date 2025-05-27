### Typing

Static languages it's explicit

python
```python
ll = [4,5,6,7]
type(ll)
```
javascript
```javascript
const ll = [4,5,6,7];
typeof(ll);
```


Type Checkers
-------------

Static languages - part of language
Synamic languages - separate program


```python
# GitHub/python/typing/[Define a JSON type](https://github.com/python/typing/issues/182)
#   Guido Says: "won't do - not needed" and closed the issue.
type JsonPrimitives = str | int | float | bool | None
type Json = Mapping[str, Json | JsonPrimitives] | Sequence[Json | JsonPrimitives]

# TEST EXAMPLE - creating is fine - reading is not (because we don't know the type)
test: Json = {
    'a': 1,
    'b': 1.1,
    'c': {'cc': 4, 'dd': {'ccc': ''}},
    'd': [1, 2.0, True, {}, []],
}
test['c']['dd']['ccc']   # nested dicts reads fail the type checker
```

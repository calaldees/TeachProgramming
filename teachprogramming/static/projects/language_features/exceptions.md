
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


---

Rethrow from
```python
    except Exception as e:
        raise RadioShowRepositoryError(
            f'Error Fetching Radio show with ID {id_}'
        ) from e
```

---

* Exceptions blast through the type system
* Can't be formally checked (no static analysis)
* Values as errors
  * (like GoLang - always returned)
  * Union types? (python)
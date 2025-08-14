Error Handling
==============

try catch else
---------

Kind of sucks - but is pervasive

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


* [(On | No) syntactic support for error handling](https://go.dev/blog/error-syntax)
  * Go team say 'no' to new error syntax
  * Don't worry if its verbose ... LLM's can write it for you (!? :laughing:)
    > Writing repeated error checks can be tedious, but today’s IDEs provide powerful, even LLM-assisted code completion.
  * > Bryan Cantrill said it might be better to title the article “Putting the ‘Go’ back into ‘Go f**k yourself’”

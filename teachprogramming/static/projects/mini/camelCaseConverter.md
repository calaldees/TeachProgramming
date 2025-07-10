
https://www.reddit.com/r/learnpython/comments/12hlv0s/would_love_some_feedback_conversion_from/
list comps


why not use regex?

```python
import re

def camel_to_snake(text: str) -> str:
    """
    >>> camel_to_snake('helloEverybodyItsTime')
    'hello_everybody_its_time'
    """
    return re.sub(r'[A-Z]', lambda match: '_' + match.group().lower(), text)


def snake_to_camel(text: str) -> str:
    """
    >>> snake_to_camel('hello_everybody_its_time')
    'helloEverybodyItsTime'
    """
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), text)
```
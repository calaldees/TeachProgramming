Prefer 'immutable collections'/'generator comprehensions' over 'incrementally constructing mutable collections'
======

I commonly see the following pattern
```python
def get_mylist(items):
    mylist = []
    for i in items:
        if some_criteria(i):
            mylist.append(some_transform(i))
    return mylist
```
The pattern is:
1. creating an empty mutable collection
2. incrementally adding to the mutable collection
3. finally returning the mutable type

I want to convey my thoughts on why this is bad pattern and suggest alternatives.

A simple case refactor of the above pattern could be:
```python
def get_mylist(items: Iterable[T]) -> Sequence[T]:
    return tuple(
        some_transform(i)
        for i in items
        if some_criteria(i)
    )
```
This helps slightly with:
* The top level collection being immutable
* The output is typed with generics


### Another example of a weak code pattern

Sometimes the `some_transform` or `some_criteria` are more complicated;
possible multiple `if` statements or `match`, possibly nested loops or function calls..

### Example of the original approach - Mutable List appending

```python
def build_my_list_of_stuff(data) -> list[MyContent]:
    results: list[MyContent] = []
    for i in data:
        match i['contentType']:
            case MyType.A:
                results.append(
                    A('some stuff', i)
                )
            case MyType.B:
                results.append(
                    B('other stuff', i)
                )

    return results
```

* In describing our loop/logic we've contaminated the iteration with lots of weighty syntax and additional indentation.
* We have multiple `append`s. Depending on the cyclomatic complexity and layout, it's not clear that all paths result in an append.
* There could be `return`s, `continue`s or `break`s in the flow.

#### Possible simplistic refactor

```python
ITEM_BUILDERS = {
    MyType.A: lambda i: A('some stuff', i)
    MyType.B: lambda i: B('other stuff', i)
}
def build_my_list_of_stuff(data) -> Sequence[MyContent]:
    return tuple(  # choose my container implementation
        ITEM_BUILDERS[i['contentType']]  # map
        for i in data
        if 'magic' in i['bits']  # filter
    )
```

* The loop remains concise and focused. I can now identify the other processing (map/filter) operations and dig further.


### Prefer Immutable types over Mutable

There is more to discuss, but at this point I can describe some observations ...

* The pattern is expandable with data structure (we can add new ways of processing without expanding a match/case structure with additional indentation and the weight of extra cases).
    * Bonus: `ITEM_BUILDERS` could even be modular at runtime if the complexity is required. It's potentially plugin-able. (looking further; using a module level dict is also not a brilliant pattern. Suggest a `register` function or decorator to register processing)
* Less room for weirdness - more understandable/grok-able
    * Cognitively, we can see that this is a transform (List of things -> Transform -> New list of things). There are no surprises, special cases, odd control flows.
    * Each append, extend, or mutation step introduces implicit state, increasing the risk of side-effects, especially if:
        * The function grows beyond the simple loop.
        * A future refactor introduces early return or continue, creating subtle bugs.
* Using [Collections Abstract Base Classes](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes) as type hints, documents how this data is intended to be used in future
    * `Collection`, `Iterable`, `Sequence`, `MutableSequence`, `Set` (Note how all intention of mutability collections are clearly labeled in the type name)
    * `collection.abc` are correct. `typing` uses the same abstract names, but is wrong!
        * `typing.Set` is mutable `collection.abc.Set` is immutable
        * I know I spoke at a previous workgroup about `import typing as t` -> `t.Set`. I was talking in old world terms; `typing` is deprecated in favor of `collection.abc`.
* I can choose my collection implementation type (in my example above I used immutable `tuple`, but this could be `frozenset` depending on use case)
* Potential for test in isolation
    * Incremental construction ties the creation and accumulation logic together. You can't easily extract or test the transformation logic independently.
* Reuse Is Harder
    * When using comprehensions or generator-based patterns, you can extract the transform/filter logic into reusable functions or pipelines. With mutable accumulation, reuse often involves manually re-copying loop+append patterns.
* Thread-Safety / Concurrency Pitfalls
    * While not always relevant, mutable state can lead to subtle bugs in concurrent code. Favoring immutability minimizes this class of issue entirely.
* If you must incrementally construct a mutable collection consider using `reduce()` as this names/signposts the pattern correctly for other developers and prevents some of the weird/surprising cases of early escapes, etc.
    * The reducer function is unit testable (see test isolation above)


### General rules (summary)

* Prefer comprehensions over incrementally building mutable structures where possible
    * Keep iteration logic tight
* Prefer Immutable types over mutable variants where possible
* Prefer Set's if order is not important. This helps document/hint at how this data is intended to be used
* In order of precedence prefer `Collection[T]`or`Generator[T]` > `Sequence/Set/Mapping` > `MutableSequence/MutableMapping/MutableSet` > `ImplementationType` when possible
    * Prefer `Collection[T]`or`Generator[T]` over `Iterable` in most cases
        * Don't mask a `Generator` as an `Iterable`. This can't be iterated over multiple times and obscures this constraint to others.
* Try not to use logic (`if`, `match/case`) to express a data structures - use lookups in preference
    * See Sam's argument that expands on this:
        * > Prefer polymorphism if you expect the number of types to increase, prefer switch if you expect the number of operations on those types to increase.
* When incremental mutable construction is required, use the `reduce` pattern for clarity


### Arguments

* Q: Could just convert it at the end? e.g `ll = [] ; ll.append('a')` then `tuple(ll)`?
    * A: This feels like a waste of allocation. Why build 65,000 items and then traverse them again in memory to form a new structure. That's unneeded.
* Q: I don't see how this helps composition? I'm still returning a collection and now I've had to spend more time typing types that I don't think bring value. A `list` is simpler
    * A: Composition is hard(er) in python, see below for some chaining ideas


### Side Quest: Generators vs Rendered Collections?

We may not need to return a `Collection`. Could we return an `Iterable`/`Generator`?
* Generators process items 'as needed':
    * Advantages:
        1. We don't have the memory overhead of keeping all rendered items in memory before moving to the next stage of processing. 
        2. We can chain generators together effectively
    * Disadvantages:
        * Debugging becomes harder
        * We can only iterate though our generator once, that may not be desirable as we don't know what downstream operations may need to be performed.


Chaining/Composing in python (My untyped old experiment)
--------

* Other languages
    * Java (Streams)
        * https://docs.oracle.com/en/java/javase/22/core/filter-processes-streams.html
    * C# (Linq)
        * https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.select
        * c sharp elevated these to language keywords
            * https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/select-clause


```python
# Hypothetical
tuple(map(filter(group((map(source))))))
#                                  ^^^^^ !? I hate this .. I hate you python .. why do you do this to us!
```

If dirty little plain javascript can do this in the core language, then python needs to sort itself out.
```javascript
[1,2,3,4,5].map(i=>i+1).filter(i=>i>3)
```


My dumb old python experiment without typing.
Chaining iterators into reuseable pipelines

https://github.com/calaldees/libs/blob/336ff630a69c38447b6f29dabcab9964e8b48b11/python3/calaldees/iterator.py#L45

I've used this in audio decode streaming (bytes to 16bit/24bit audio ints) and cryptographic demo processing of incoming stream (input encrypted --- output decrypted)


### Chains - can you go too far?

Frameworks like RxJava encourage long pipelines/chains. When used to the extreme they can make data processing inflexible and difficult to debug. As with all patterns then can be abused/misused.


What about exceptions?
---------------------

Oh python .. you do make this hard ..
The more I work with exceptions, the more I hate the pattern, they break program flow and destroy the type system.

```python
from collections.abc import Callable
from typing import Type, Tuple

type ExceptionTypes = Tuple[Type[BaseException]]


def replace_exception[T](
    original: Callable[[T], T],
    default: T | None = None,
    exception_types: ExceptionTypes = (Exception,),
) -> Callable[[T], T | None]:
    """
    >>> timezone = 'timezone'
    >>> def _build_block(b, another_param):
    ...     if b == 'error':
    ...         raise Exception('test')
    ...     return b
    >>> tuple(filter(None, map(replace_exception(lambda i: _build_block(i, timezone)), ['a','error','c'])))
    ('a', 'c')

    """
    def _safe(t: T) -> T | None:
        try:
            return original(t)
        except exception_types:
            return default

    return _safe

```


Reduce Pattern
--------------

If you really need to construct a mutable type, this can be done with the `reduce` pattern.

TODO: arguments to use reduce

```python
from itertools import reduce

def reducer():
reduce(reducer, collection, {})
```


Grouping Pattern
----------------

TODO: Finish
Grouping with append pattern?
Consider ways of optimizing this, this is super common

```python
    boosted_blocks = []
    candidate_blocks = []
    # `feature` could be typed ()`dict[Any]`?) and maybe renamed to `raw_feature_data`
    # `.blocks_key` to be replaced with `get_audience_block_lists` - see notes in `UpstreamPlatform` for suggestions.
    for block in platform.normalize_blocks(feature):
        if block.boosted:
            boosted_blocks.append(block)
        else:
            candidate_blocks.append(block)
```




---

## Original Code for review


```python
from enum import StrEnum
from typing import Sequence, TypedDict


class Image(TypedDict):
    url: str
    alt: str


class BaseContent(TypedDict):
    content_type: str
    universal_link: str
    title: str
    image: Image


class Video(BaseContent):
    publish_date: str


class Playlist(BaseContent):
    genre: str


class Podcast(BaseContent):
    itunes_author: str


class Article(BaseContent):
    is_breaking_news: bool
    is_live_news: bool
    is_exclusive: bool
    publish_date: str


class ContentType(StrEnum):
    Video = 'VIDEO'
    Playlist = 'PLAYLIST'
    Podcast = 'PODCAST'
    Article = 'ARTICLE'


class SearchResponse(TypedDict):
    results: Sequence[BaseContent]


def build_search_response(search_data) -> SearchResponse:
    results: list[BaseContent] = []
    for result_item in search_data:
        match result_item['contentType']:
            case ContentType.Video:
                results.append(
                    Video(
                        content_type=result_item['contentType'].title(),
                        universal_link=result_item['universalLink'],
                        publish_date=result_item['publishDate'],
                        title=result_item['title'],
                        image=result_item['image'],
                    )
                )
            case ContentType.Playlist:
                genres = result_item['genres']
                genre = genres[0]['name'] if genres else ''
                results.append(
                    Playlist(
                        content_type=result_item['contentType'].title(),
                        universal_link=result_item['universalLink'],
                        title=result_item['title'],
                        genre=genre,
                        image=result_item['image'],
                    )
                )
            case ContentType.Podcast:
                results.append(
                    Podcast(
                        content_type=result_item['contentType'].title(),
                        universal_link=result_item['universalLink'],
                        title=result_item['title'],
                        itunes_author=result_item['itunesAuthor'],
                        image=result_item['image'],
                    )
                )
            case ContentType.Article:
                results.append(
                    Article(
                        content_type=result_item['contentType'].title(),
                        universal_link=result_item['universalLink'],
                        is_breaking_news=result_item['isBreakingNews'],
                        is_live_news=result_item['isLiveNews'],
                        is_exclusive=result_item['isExclusive'],
                        publish_date=result_item['publishDate'],
                        title=result_item['title'],
                        image=result_item['image'],
                    )
                )
    return SearchResponse(results=results)

```


Thought:
I'm looking at this case logic and thinking that this is a data problem and not a flow/logic problem.
I'm finding it hard to grok what's going on. I don't have much context for brand_config and can see we are inserting things if we have an app in the config.

I kind of feel that rather than lots of cases and appends. We could have one set of logic with data for each band app. e.g.
We should attempt to avoid incremental appends and use a comprehension of some sort in preference.
To avoid the extra layer of if/case, I think the code below solves the problem in less lines.


Diff Noise and Code Churn
In long for loops with many if/match/append statements, adding a new branch causes large diffs—touching multiple lines. This is worse for reviews and version control than a clean dict/lookup or a declarative mapping.



## Refactor 1

```python
# My first pass
_BUILD_SEARCH_RESULT_FROM_RESPONSE_ITEM = MappingProxyType({
    ContentType.Video: lambda i: Video(
        content_type=i['contentType'].title(),
        universal_link=i['universalLink'],
        publish_date=i['publishDate'],
        title=i['title'],
        image=i['image'],
    )
    ContentType.Playlist: lambda i: Playlist(
        content_type=i['contentType'].title(),
        universal_link=i['universalLink'],
        title=i['title'],
        genre=i['genres'][0]['name'] if i['genres'] else '',
        image=i['image'],
    )
    ContentType.Podcast: lambda i: Podcast(
        content_type=i['contentType'].title(),
        universal_link=i['universalLink'],
        title=i['title'],
        itunes_author=i['itunesAuthor'],
        image=i['image'],
    )
    ContentType.Article: lambda i: Article(
        content_type=i['contentType'].title(),
        universal_link=i['universalLink'],
        is_breaking_news=i['isBreakingNews'],
        is_live_news=i['isLiveNews'],
        is_exclusive=i['isExclusive'],
        publish_date=i['publishDate'],
        title=i['title'],
        image=i['image'],
    )
})
def build_search_response(search_data) -> SearchResponse:
    return SearchResponse(results=tuple(
        _BUILD_SEARCH_RESULT_FROM_RESPONSE_ITEM[i['contentType']](i)
        for i in search_data
    ))
```

## Refactor 2

```python
# Second pass
# Move the parsing/conversion to the object itself? (maybe move these from TypedDict's to NamedTuple? or Dataclass to allow class methods?)
_TYPE_LOOKUP = MappingProxyType({
    ContentType.Video: Video.from_response,
    ContentType.Playlist: Playlist.from_response
    ContentType.Podcast: Podcast.from_response
    ContentType.Article: Article.from_response,
})
def build_search_response(search_data) -> SearchResponse:
    return SearchResponse(results=tuple(
        _TYPE_LOOKUP[i['contentType']](i)
        for i in search_data
    ))

```

```python
# third pass
def _build_search_results(result_item):
    ... # todo - some kind of simple factory?
def build_search_response(search_data) -> SearchResponse:
    return SearchResponse(results=tuple(map(_build_search_results, search_data)))
```


Other Examples
==============

karakara
```
    targets = []
    for tr in tracks:
        for t in tr.targets:
            targets.append(t)
```
```
    targets = tuple(
        target
        for tr in tracks
        for target in tr.targets
    )
```
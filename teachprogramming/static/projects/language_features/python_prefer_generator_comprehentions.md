Prefer generator comprehensions or immutable collections over incrementally creating mutable collections
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
The pattern is creating an empty mutable collection, followed by incrementally adding to the mutable collection, and then finally returning the mutable type.

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
This helps with the top level collection being immutable.


### Real example

Sometimes the `some_transform` or `some_criteria` is implemented with multiple `if` statements or `match`.

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

### Prefer Immutable types over Mutable

The benefits of the approach above:

* The pattern is expandable with data structure (we can add new ways of processing without expanding a big match/case structure). This could even be modular at runtime if the complexity is required. It's potentially plugin-able.
* Less room for weirdness - more understandable/grok-able
    * Cognitively, we can see that this is a straight transform (List of things -> Transform -> New list of things). There are no surprises, special cases, odd control flows.
    * Each append, extend, or mutation step introduces implicit state, increasing the risk of side-effects, especially if:
        * The function grows beyond the simple loop.
        * A future refactor introduces early return or continue, creating subtle bugs.
* Using [Collections Abstract Base Classes](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes) as type hints, documents how this data is intended to be used in future
    * `Collection`, `Iterable`, `Sequence`, `MutableSequence`
* I can choose implementation type (in my example above I used immutable `tuple`, but this could be `frozenset` depending on use case)
* Harder to Test in Isolation
    * Incremental construction ties the creation and accumulation logic together. You can't easily extract or test the transformation logic independently.
* Reuse Is Harder
    * When using comprehensions or generator-based patterns, you can extract the transform/filter logic into reusable functions or pipelines. With mutable accumulation, reuse often involves manually re-copying loop+append patterns.
* Thread-Safety / Concurrency Pitfalls
    * While not always relevant, shared mutable state can lead to subtle bugs in concurrent code. Favoring immutability minimizes this class of issues entirely.


### General rules (summary)

* Prefer comprehensions over incrementally building mutable structures where possible
* Prefer Immutable types over mutable variants where possible
* Prefer Set's if order is not important. This helps document/hint at how this data is intended to be used
* In order of precedence prefer `Iterable`/`Generator` > `Collection` > `Sequence/Set`
    * A `Collection` is `Iterable` and can be iterated over multiple times
    * I would prefer to explicitly return `Generator` rather than masking a Generator as an `Iterable` because they can't be iterated over multiple times
* Try not to use logic (`if`, `match/case`) to express a data structures - use lookups in preference


### Arguments

* Q: Could just convert it at the end? e.g `ll = [] ; ll.append('a')` then `tuple(ll)`? A: This feels like a waste of allocation. Why build 65,000 items and then traverse them again in memory to form a new structure. That's unneeded.



### Side Quest: Generators vs Rendered Collections?

We may not need to return a `Collection`. Could we return an `Iterable`/`Generator`? 
* Generators process items 'as needed':
    * Advantages:
        1. We don't have the memory overhead of keeping all rendered items in memory before moving to the next stage of processing. 
        2. We can chain generators together effectively
    * Disadvantages:
        * Debugging becomes harder
        * We can only iterate though our generator once, that may not be desirable as we don't know what downstream operations may need to be performed.


Chaining
--------

Inspired by Java (Streams) and C# (Linq)

My dumb old python experiment without typing.
Chaining iterators into reuseable pipelines


```python
# Hypothetical
tuple(map(filter(group((map(source))))))
#                                  ^^^^^ !? I hate this .. I hate you python .. why do you do this to us!
```

https://github.com/calaldees/libs/blob/336ff630a69c38447b6f29dabcab9964e8b48b11/python3/calaldees/iterator.py#L45

If plain javascript can do this in the core language
```javascript
[1,2,3,4,5].map(i=>i+1).filter(i=>i>3)
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
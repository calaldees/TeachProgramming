
I am writing an article for a team of professional python programmers.

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

### Mutable original

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
* Using [Collections Abstract Base Classes](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes) as type hints, documents how this data is intended to be used in future
    * `Collection`, `Iterable`, `Sequence`, `MutableSequence`
* I can choose implementation type (in my example above I used immutable `tuple`, but this could be `frozenset` depending on use case)


### General rules (summary)

* Prefer comprehensions over incrementally building mutable structures where possible
* Prefer immutable types over mutable variants where possible
* Prefer iterables in preference to collections where possible (unless you know you will need to traverse the collection multiple times)
* Try not to use logic (`if`, `case`) to express a data structures - use lookups in preference


### Arguments

* Q: Could just convert it at the end? e.g `ll = [] ; ll.append('a')` then `tuple(ll)`? A: This feels like a waste of allocation. Why build 65,000 items and then traverse them again in memory to form a new structure. That's unneeded.



### Side Quest: Generators vs Rendered Collections?

We don't need to return a `Collection`. Could we return an `Iterable`/`Generator`

* Generators process items 'as needed':
    * Advantages:
        1. We don't have the memory overhead of keeping all rendered items in memory before moving to the next stage of processing. 
        2. We can chain generators together effectively
    * Disadvantages:
        * Debugging becomes harder
        * We can only iterate though our generator once, that may not be desirable as we don't know what downstream operations may need to be performed.




---

Thought:
I'm looking at this case logic and thinking that this is a data problem and not a flow/logic problem.
I'm finding it hard to grok what's going on. I don't have much context for brand_config and can see we are inserting things if we have an app in the config.

I kind of feel that rather than lots of cases and appends. We could have one set of logic with data for each band app. e.g.
We should attempt to avoid incremental appends and use a comprehension of some sort in preference.
To avoid the extra layer of if/case, I think the code below solves the problem in less lines.



---



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

Reduce Pattern
==============



Grouping Pattern
================

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
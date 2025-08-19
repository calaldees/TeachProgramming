

TypeDict
dataclass
NamedTuple

TypeDict
[NotRequired](https://docs.python.org/3/library/typing.html#typing.NotRequired)

[python dataclasses with optional attributes](https://stackoverflow.com/a/72582101/3356840)
> It's not possible to use a dataclass to make an attribute that sometimes exists and sometimes doesn't because the generated __init__, __eq__, __repr__, etc hard-code which attributes they check.
> However, it is possible to make a dataclass with an optional argument that uses a default value for an attribute (when it's not provided).

